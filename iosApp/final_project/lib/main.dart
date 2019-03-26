import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class Dialogue{
  information(BuildContext context, String title, String description){
    return showDialog(
      context: context,
      barrierDismissible: true,
      builder: (BuildContext context){
        return AlertDialog(
          title: Text(title),
          content: SingleChildScrollView(
            child: ListBody(
              children: <Widget>[
                Text(description)
              ],
            ),
          ),
          actions: <Widget>[
            FlatButton(
              onPressed: () => Navigator.pop(context),
              child: Text('Ok'),
            )
          ],
        );
      },
    );
  }
}

class MyApp extends StatelessWidget {
  Dialogue dialogues = new Dialogue();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Music Genre Classifier',
      theme: ThemeData(

        primarySwatch: Colors.red,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('Music Genre Classifier'),
        ),
        body: Center(
          child: new RawMaterialButton(
            onPressed: (){
              dialogues.information(context, 'Title', 'Description');
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
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);


  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {

      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(

        title: Text(widget.title),
      ),
      body: Center(
        child: Column(

          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.display1,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}
