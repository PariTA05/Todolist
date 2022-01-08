import 'package:flutter/material.dart';


//package for http method
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class UpdatePage extends StatefulWidget {
  final v1,v2,v3;
  const UpdatePage(this.v1,this.v2,this.v3);

  @override
  _UpdatePageState createState() => _UpdatePageState();
}

class _UpdatePageState extends State<UpdatePage> {

  var _v1, _v2, _v3;
    //ประเภทตัวแปลที่เราต้องการเก็บ
  TextEditingController todo_title = TextEditingController();  
  TextEditingController todo_detail = TextEditingController();

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _v1 = widget.v1;  //id
    _v2 = widget.v2;  //title
    _v3 = widget.v3;  //detail
    todo_title.text = _v2;
    todo_detail.text = _v3;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Edit List'),
      actions: [
          IconButton(onPressed: () {
            print("Delect ID : $_v1");
            deleteTodo();

            //back autometic to home page
            Navigator.pop(context, 'delete');

          }, icon: Icon(Icons.delete,color: Colors.red,))
      ],),

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
                  updateTodo();
                  final snackBar = SnackBar(
                      content: const Text('Already Update'),);
                    ScaffoldMessenger.of(context).showSnackBar(snackBar);

                },
                child: Text("Edit List"),
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


  Future updateTodo() async {
    // var url = Uri.https('f26e-124-120-178-16.ngrok.io','/api/post-todolist');
    var url = Uri.http('192.168.1.50:8000','/api/update-todolist/$_v1');  //local host
    Map<String, String> header = {"Content-type":"application/json"};
    String jsondata = '{"title":"${todo_title.text}", "detail":"${todo_detail.text}"}';
    var response = await http.put(url, headers: header, body: jsondata);
    print('-------result----------');
    print(response.body);
  }


  Future deleteTodo() async {
    var url = Uri.http('192.168.1.50:8000','/api/delete-todolist/$_v1');  //local host
    Map<String, String> header = {"Content-type":"application/json"};
    var response = await http.delete(url, headers: header);
    print('-------result----------');
    print(response.body);
  }


}

