from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

#GET DATA
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #select data from Todolist model same as SQL "select*from todolist"
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#POST DATA (save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#PUT DATA (Update data) #TID=TodolistID
@api_view(['PUT'])
def update_todolist(request,TID):
    #getคือการดึงตามID --> data localhost:8000/update-todolist/(TID)
    todo = Todolist.objects.get(id=TID)  

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'update'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#Delete DATA 
@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)  

    if request.method == 'DELETE' :
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)










data = [
    {
        "title":"Harbin Ice Festival",
        "subtitle":"เทศกาลทศกาลหิมะ ที่มีชื่อเสียงที่สุดของเมืองฮาร์บิน",
        "image_url":"https://raw.githubusercontent.com/PariTA05/BasicAPI/main/HarbinIceFestival.jpg",
        "detail":"งานเทศกาลประติมากรรมหิมะและน้ำแข็งcHarbin International Ice and Snow Sculpture Festivalcจัดขึ้นเป็นประจำทุกปีมาตั้งแต่ พ.ศ.2528 โดยจะจัดขึ้นช่วงมกราคมถึงกุมภาพันธ์ มีระยะเวลา 1 เดือนกิจกรรมในช่วงเวลาเทศกาลมีทั้งการแข่งขันสกี Yabuli Alpine การแข่งขันว่ายน้ำในแม่น้ำซงหัว และนิทรรศการโคมน้ำแข็งในสวนเจ้าหลิน ซึ่งงานเทศกาลนี้นับว่าเป็นงานเทศกาลหิมะและน้ำแข็งที่ใหญ่ ติดอันดับ 1 ใน 4 ของทั้งโลก ซึ่งสามารถดึงนักท่องเที่ยวจากทั่วทุกมุมโลกมาเยี่ยมชมงานนี้เป็นจำนวนมาก เทศกาลน้ำแข็งนานาชาติ เมืองฮาร์บิน Harbin Ice and Snow Festival ความสวยงามตระการตาของงานประติมากรรมน้ำแข็ง ในหลากหลายรูปแบบ นักท่องเที่ยวจะได้สัมผัสกับงานประติมากรรมน้ำแข็ง ที่น่าตื่นตาตื่นใจ ไม่ว่าจะเป็นพระราชวัง โบสถ์และเจดีย์ ท่ามกลางแสงสีที่วิจิตรสวยงาม ไฮไลท์ของอยู่ที่หอคอยที่โดดเด่นซึ่งเป็นที่สูงไม่น้อยกว่า 26 เมตร และประมาณ 20 ชั้นเป็นหนึ่งในสถานที่ท่องเที่ยวสำคัญในงานเทศกาล ซึ่งสร้างด้วยน้ำแข็งที่นำมาแกะสลักแต่ละชิ้น บางชิ้นสูงถึง 26 เมตร และกว้าง 117 เมตร เรียกได้ว่าอลังการงานสร้างสุดๆ ในยามค่ำคืน น้ำแข็งที่ถูกนำมาสร้างเป็นหอคอย ปราสาท หรืออื่นๆ จะถูกประดับด้วยแสงไฟ สร้างสีสันให้กับนักท่องเที่ยวได้มากทีเดียว "
    },
    {
        "title":"St.Sophia Cathedral",
        "subtitle":"แลนด์มาร์คอันดับ 1 ของเมืองฮาร์บิน",
        "image_url":"https://raw.githubusercontent.com/PariTA05/BasicAPI/main/St.SophiaCathedral.jpg",
        "detail":"โบสถ์เซนต์โซเฟีย ถือเป็นแลนด์มาร์คอันดับ 1 ของเมืองฮาร์บินเลยก็ว่าได้ ซึ่งโบสถ์แห่งนี้ถือเป็นโบสถ์คริสต์สไตล์รัสเซียที่สร้างขึ้นตามแบบฉบับของการสร้างโบสถ์รัสเซียจริงๆ สมัยก่อนใช้เป็นสถานที่ประกอบพิธีกรรมทางศาสนาของทหารรัสเซียเมื่อครั้งเข้ามายึดครองเมืองฮาร์บิน โดยในปัจจุบันภายในโบสถ์เซนต์โซเฟียแห่งนี้เป็นพิพิธภัณฑ์ที่จัดแสดงรูปภาพและประวัติของเมืองฮาร์บินในยุกต์ต่างๆ"
    },
    {
        "title":"Zhongyand Street",
        "subtitle":"ถนนจงยางไฮไลท์ในไฮไลท์ของเมืองฮาร์บิน",
        "image_url":"https://raw.githubusercontent.com/PariTA05/BasicAPI/main/ZhongyandStreet.jpg",
        "detail":"ถนนจงยางบอกได้คำเดียวว่าเป็นสถานที่ที่โครตจะโรแมนติก ถนนเส้นนี้มีความยาว 1.4 กม ถ้าเดินจากหัวถนนไปจนสุดจะเจอกับแม่น้ำซงฮัวเจียงที่จะกลายเป้นน้ำแข็งทั้งสายในช่วงฤดูหนาวสองข้างถนนเต็มไปด้วยร้านกาแฟ ร้านขายของกิน ของที่ระลึงของเมืองฮาร์บิน ช่วงฤดูหนาวจะมีการประดับด้วยโคมไฟน้ำแข็งที่แกะสละมาอย่างสวยงามเพื่อต้อนรับนักท่องเที่ยว แต่บอกไว้เลยว่าใครไปเดินเล่นที่นี้ช่วงฤดูหนาว ให้เตรียมอุปกร์ณกันหนาวดีเพราะหนาวมาก"
    },
    {
        "title":"harbin grand theatre",
        "subtitle":"โรงโอเปร่าขนาดใหญ่ของเมืองฮาร์บิน",
        "image_url":"https://raw.githubusercontent.com/PariTA05/BasicAPI/main/HarbinGrandTheatre.jpg",
        "detail":"โรงโอเปร่าที่สามารถจุคนได้ถึง 1,600 คน โดยทางทีมสถาปนิกได้ออกแบบให้ โรงโอเปร่าฮาร์บินแห่งนี้ เป็นศูนย์วัฒนธรรมแห่งอนาคตที่พรั่งพร้อมไปด้วยส่วนจัดแสดงที่กว้างขวาง และเป็นพื้นที่สาธารณะที่รวมความเป็นมนุษย์ ศิลปะ และเอกลักษณ์ของเมืองฮาร์บินเข้าด้วยกันกับธรรมชาติโดยรอบ เป็นอีกหนึ่งสถานที่แห่งจินตนาการที่ทันสมัยและสวยงามจริงๆ"
    }
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})
