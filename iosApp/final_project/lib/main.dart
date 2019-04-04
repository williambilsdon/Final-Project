import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';


void main() => runApp(MyApp());

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Music Genre Classifier',
      theme: ThemeData(

        primarySwatch: Colors.red,
      ),
      home: Result()
    );
  }
}

class Result extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Music Genre Classifier'),
      ),
      body: Center(
        child: new RawMaterialButton(
          onPressed: (){
            showDialog(
                context: context,
                builder: (_) => new AlertDialog(
                  title: new Text("Genre:", textAlign: TextAlign.center),
                  content: new Text("Example", textAlign: TextAlign.center),
                  actions: <Widget>[
                    // usually buttons at the bottom of the dialog
                    new FlatButton(
                      child: new Text("Close"),
                      onPressed: () {
                        Navigator.of(context).pop();
                      },
                    ),
                  ],
                )
            );
          },

          child: new Icon(
            Icons.mic,
            color: Colors.white,
            size: 60.0,
          ),
          shape: new CircleBorder(),
          elevation: 2.0,
          fillColor: Colors.red,
          padding: const EdgeInsets.all(15.0),
        ),
      ),
      bottomNavigationBar: BottomAppBar(
        child: Container(
            height: 75,
            color: Colors.red
        ),
      ),
    );
  }
}


