import 'dart:async';
import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter_timer/ticker.dart';

part 'timer_event.dart';
part 'timer_state.dart';

class TimerBloc extends Bloc<TimerEvent, TimerState> {
  final Ticker _ticker;
  static const int _duration = 60;

  StreamSubscription<int>? _tickerSubscription;

  void _onStarted(TimerStarted started, Emitter<TimerState> emit) {
    emit(TimerRunInProgress(started.duration));

    _tickerSubscription?.cancel();
    _tickerSubscription = _ticker
        .tick(ticks: started.duration)
        .listen((duration) => add(TimerTicked(duration: duration)));
  }

  void _onTicked(TimerTicked ticked, Emitter<TimerState> emit) {
    emit(
      ticked.duration > 0
          ? TimerRunInProgress(ticked.duration)
          : const TimerRunComplete(),
    );
  }

  void _onPaused(TimerPaused paused, Emitter<TimerState> emit) {
    if (state is TimerRunInProgress) {
      _tickerSubscription?.pause();
      emit(TimerRunPause(state.duration));
    }
  }

  void _onResumed(TimerResumed resume, Emitter<TimerState> emit) {
    if (state is TimerRunPause) {
      _tickerSubscription?.resume();
      emit(TimerRunInProgress(state.duration));
    }
  }

  void _onReset(TimerReset reset, Emitter<TimerState> emit) {
    _tickerSubscription?.cancel();
    emit(const TimerInitial(_duration));
  }

  TimerBloc({required Ticker ticker})
      : _ticker = ticker,
        super(const TimerInitial(_duration)) {
    on<TimerStarted>(_onStarted);
    on<TimerResumed>(_onResumed);
    on<TimerTicked>(_onTicked);
    on<TimerPaused>(_onPaused);
    on<TimerReset>(_onReset);

    @override
    Future<void> close() {
      _tickerSubscription?.cancel();
      return super.close();
    }
  }
}
