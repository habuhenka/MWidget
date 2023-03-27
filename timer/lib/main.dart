import 'package:bloc/bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_timer/observer.dart';

import 'app.dart';

void main() {
  BlocOverrides.runZoned(
    () => runApp(const App()),
    blocObserver: BlocObserve(),
  );
}
