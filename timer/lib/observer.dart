import 'package:bloc/bloc.dart';
import 'package:flutter_timer/timer/timer.dart';

class BlocObserve extends BlocObserver {
  @override
  void onEvent(Bloc bloc, Object? event) {
    super.onEvent(bloc, event);
    print("onEvent = $event");
  }

  @override
  void onError(BlocBase bloc, Object error, StackTrace stackTrace) {
    super.onError(bloc, error, stackTrace);
    print("onError = ${bloc.runtimeType}, $error, $stackTrace");
  }

  @override
  void onChange(BlocBase bloc, Change change) {
    super.onChange(bloc, change);
    // print("onChange = ${bloc.runtimeType}, $change");
  }

  @override
  void onTransition(Bloc bloc, Transition transition) {
    super.onTransition(bloc, transition);
    print("onTransition = $transition");
  }
}
