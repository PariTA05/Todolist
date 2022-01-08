import 'package:flutter/material.dart';

//package for http method
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class AddPage extends StatefulWidget {
  const AddPage({ Key? key }) : super(key: key);

  @override
  _AddPageState createState() => _AddPageState();
}

class _AddPageState extends State<AddPage> {
  //ประเภทตัวแปลที่เราต้องการเก็บ
  TextEditingController todo_title = TextEditingController();  
  TextEditingController todo_detail = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Add New List'),),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView(
          children: [
            //ช่องกรอกข้อมูล title and detail
            TextField(
              controller: todo_title,
              decoration: InputDecoration(
              labelText: 'Planned', 
              border: OutlineInputBorder())),

            SizedBox(height: 30,),
            TextField(
              minLines: 4,
              maxLines: 8,
              controller: todo_detail,
              decoration: InputDecoration(
              labelText: 'Detail', 
              border: OutlineInputBorder())),
            SizedBox(height: 30,),
            //ปุ่มเพิ่มข้อมูล
            Padding(
              padding: const EdgeInsets.fromLTRB(100, 20, 100, 20),
              child: ElevatedButton(
                onPressed: () {
                  print('------------');
                  print('title: ${todo_title.text}');
                  print('detail: ${todo_detail.text}');
                  postTodo();
                  setState(() {
                    todo_title.clear();
                    todo_detail.clear();
                  });
                },
                child: Text("Add List"),
                style: ButtonStyle(
                  backgroundColor:
                    MaterialStateProperty.all(Colors.blue[700]),
                  padding: 
                    MaterialStateProperty.all(EdgeInsets.fromLTRB(50, 10, 50, 10)),
                  textStyle:
                    MaterialStateProperty.all(TextStyle(fontSize: 20))
                ),
              ),
            ),
          ],
        ),
      )
    );
  }
  Future postTodo() async {
    // var url = Uri.https('f26e-124-120-178-16.ngrok.io','/api/post-todolist'); // NGLOG
    var url = Uri.http('192.168.1.50:8000','/api/post-todolist');  //local host IP
    Map<String, String> header = {"Content-type":"application/json"};
    String jsondata = '{"title":"${todo_title.text}", "detail":"${todo_detail.text}"}';
    var response = await http.post(url, headers: header, body: jsondata);
    print('-------result----------');
    print(response.body);
  }
}

