# Django

* 웹 프레임워크

* Python언어로 만들어졌다.
* Python 컴퓨터와 대화하는 하나의 방식
  * 데이터 분석, 머신 러닝이 가능하다.
  * 라이브러리 : 단순 활용가능한 도구들의 집합
  * 프레임 워크 : 라이브러리를 많이 가지고 있다. 
    * 도구들의 집합들을 사용할 수 있게 만들어졌다.
    * 프레임워크는 뼈대나 기반구조를 의미
    * 소프트웨어에써는 문제를 해결하기 위해서 상호 협력하는 클래스와 인터페이스의 집합
* 웹 프레임워크 django
  * 사용자 인터페이스
  * DB 연동
  * URL 파싱
  * 세션 관리
  * 관리자 페이지
  * Request 파싱 등등 가능
* 모델(Model), 템플릿(Template), 뷰(View) 
  * Django에서는 MTV패턴
* Django가 제공하는 것으로
  * 폼, 개발 프로세스, 관리자, 보안 등등을 제공한다.



# MTV 패턴

* 모델(Model), 템플릿(Template), 뷰(View) 

  * ![MTV 패턴](https://user-images.githubusercontent.com/72541544/114030603-8999e980-98b5-11eb-8d3b-2b1633333adf.png)

  * 사진 주소 : [초보자를 위한 장고 Django 뿌시기🔥 - 구름EDU (goorm.io)](https://edu.goorm.io/lecture/16377/초보자를-위한-장고-django-뿌시기)

    * Client : 클라이언트, 사용자

    * View : 요청에 대한 응답을 하는 곳

    * Template : View에서 response로 쓰이는 HTML, XML 등등

      * render 함수를 통해 template (html)을 response로 client에게 보여준다.

    * Model : DataBase에 테이블 형태로 만들기 위한 설계

      * Relation : Model 상호간의 관계
      * DataBase : 실제로 데이터를 저장하는 곳
        * DB에서는 보통 SQL 언어를 사용한다.
      * Django에서 사용하는 Python과 SQL은 다른 언어이므로 통역사가 필요하다.
        * (이를 위한) 통역사 : ORM이다.
          * Python에서 DB와 서로 소통할 수 있게 만들어 준다.

      

      * Client가 View에게 요청을 하고, View는 Client에게 응답을 한다.
      * ex) 11번가 서버 접속을 예로 든다면
      * Client가 인터넷에서 11번가 검색 후 url 접속을 시도할 때
      * Client은 11번가 서버로 요청하게 되고 서버 View 다음 Model을 거친 후 DB에서 상품 객체들을 가져와서  html로 구성된 화면에 render함수를 통해 응답으로 사용자들 화면에 띄어준다.
      * View 같은 경우 11번가 서버를 의미하고, template 보이는 화면을 의미한다.
      * Model 같은 경우 11번가 화면에 보이는 상품 이름, 가격 등을 설계해서 만들어 진 것을 상품 Model이라고 한다.
        * 이러한 상품 모델(설계)로 찍어낸 상품 하나 하나를 객체라고 한다.
        * 한쪽 방향에서는 이러한 객체들을 DB에 저장하는 과정이다.
        * 다른 방향에서는 서버에서 DB로부터 불러와서 화면 template에 뿌려주는 역할을 한다. 이를 통해 화면에 보이게 된다.
      * template 틀 화면이라 생각하면 되고, Model 같은경우 구체적인 화면 구성요소로 생각하면 된다.

  * ex)

  * User : Username, Email, Password, Bdate

    * 컬럼, 필드, 애트리뷰트 : 특정 모델의 속성들
    * 모델의 컬럼마다 데이터 타입이 있다.
    * 데이터 타입(자료형) : 프로그래밍 언어에서 실수치, 정수, 불린 자료형 따위의 여러 종류의 데이터를 식별하는 분류
    * ![UserTable](https://user-images.githubusercontent.com/72541544/114030146-34f66e80-98b5-11eb-8344-7184caa0807c.png)
    * 사진 주소 : [초보자를 위한 장고 Django 뿌시기🔥 - 구름EDU (goorm.io)](https://edu.goorm.io/lecture/16377/초보자를-위한-장고-django-뿌시기)
    * User 내용들을 migrate라는 과정을 통해 DB에 User Table을 생성한다.
      * Table : Excel 표와 비슷하다.

  * Post : Title, Content, ViewCount

    * 제목, 글 내용, 조회 수

  * Comment : content

    * 댓글

  * 이처럼 설계한 것들이 모델이고 이들로 객체를 찍어낸다.


# vscode 설정

* 먼저 git Bash를 TERMINAL에 추가한다.
* ![Terminal](https://user-images.githubusercontent.com/72541544/115647713-4a60a380-a35f-11eb-90fa-b9e1886acc54.png)
  * vscode 첫 시작시 TERMINAL 기본 쉘로 Command Prompt, PowerShell만 존재할 것이다.
  * ![terminal2](https://user-images.githubusercontent.com/72541544/115647732-50568480-a35f-11eb-8484-e2d8537f1eff.png)
* ctrl + shift + '(물결) 
  * bash 터미널 창이 뜬다.
  * ![bash](https://user-images.githubusercontent.com/72541544/115647871-8a278b00-a35f-11eb-9b8f-03f5b7782f73.png)
* vscode EXPLORER에 디렉터리를 OPEN 한다.
* 현재 TERMINAL에 git bash를 열어준다. (alt + shift + `)
* ![터미널](https://user-images.githubusercontent.com/72541544/115647726-4f255780-a35f-11eb-802b-af8eb20c6b44.png)

* 위 자료는 웹 주소 : https://integer-ji.tistory.com/81?category=745989 에서 가져온 자료입니다.



## 이제 중요

* python 버전 확인하기

  * python --version
  * 3.6 버전 이상 진행해야한다.

* venv(가상 환경) 생성하기

  * python -m venv myvenv
    * myvenv : 생성하려는 가상 환경 이름
    * 가상환경이라는 걸 쉽게 알기 위해 venv를 붙여줘야 한다.
  * 실행시 현재 디렉터리 경로에 myvenv 디렉터리가 설치된다.
  * 가상 환경(Virtual environment) : virtualenv라고도 한다.
    * 기존에 설치되어있는 Python과 django를 분리시켜 준다.
    * 다른 프로젝트들과 충돌이 안나게 독립적인 환경을 만들어 준다.

* 가상 환경 실행하기

  * source myvenv(가상 환경 이름)/Scripts/activate

  * ![source](https://user-images.githubusercontent.com/72541544/115647897-91e72f80-a35f-11eb-9f4b-93ec90cd0c3f.png)

    * 정상 실행될 시 myvenv(가상 환경 이름) 출력
      * 이제부터 myvenv 가상환경 안에 있는 것을 말하는 것이다.
      * pip, setuptools, wheel 가상환경을 시작할 때 기본으로 설치된 것이다.

    * 가상 환경을 종료하는 방법
      * deactivate 또는 터미널 종료하면 된다.

  * pip란?

    * pip는 파이썬으로 작성된 패키지 라이브러리를 관리해주는 시스템
      * 리눅스에서는 apt-get이다.
    * pip는 python 3.4 이후 버전에는 기본적으로 포함되어 있다.
    * pip list
      * 현재 내 컴퓨터에 설치된 python package 목록을 볼 수 있다.
    * pip install --upgrade pip
      * pip를 최신 버전으로 업그레이드 할 때 사용
    * pip install <패키지 이름>
      * pip를 이용해 파이썬 라이브러리 패키지를 설치
    * pip uninstall <패키지 이름>
      * pip를 이용해 설치된 패키지를 제거
    * 많이 사용하는 패키지들은 대부분 pip를 이용해 설치할 수 있다.

* Django 설치하기

  * pip install django
    * django 패키지를 설치한다.
    * 특정 버전의 django를 다운로드 하기 위해서는
      * pip install django==2.x.x 식으로 입력하면된다.

* ![pip install](https://user-images.githubusercontent.com/72541544/115647998-c0fda100-a35f-11eb-9f95-962616f68683.png)

  * 만약 설치 완료 후 업그레이드를 요구한다면
    * python -m pip install --upgrade pip를 입력해주면 된다.

* ![python upgrade](https://user-images.githubusercontent.com/72541544/115648003-c1963780-a35f-11eb-93b5-b979262650cb.png)





## Django를 이용해 project 만들고, app 생성

* pip 업그레이드가 완료되었다면 django-admin을 이용해 project를 만들어 준다.
  * django-admin startproject crudproject
    * crudproject를 생성한다.
* django 서버 작동
  * 이제 crudproject 경로로 이동하여, runserver를 한다.
  * python manage.py runserver
    * 명령어를 실행하면 기본적으로 내부 IP의 8000번 포트로 개발 서버를 띄운다.
    * manage.py를 이용하여 http://127.0.0.1:8000/ 서버가 시작된다.
    * 열린 서버를 닫을 때 : ctrl + c
    * 8080 포트 바꾸려면
      * python manage.py runserver 8080
    * 서버 IP 바꾸기
      * python manage.py runserver 0:8000
  * ![runserver](https://user-images.githubusercontent.com/72541544/115647760-577d9280-a35f-11eb-8666-6129aef0e5aa.png)
  * ![django internet](https://user-images.githubusercontent.com/72541544/115647757-56e4fc00-a35f-11eb-81bb-449707281a3c.png)
* app 만들기
  * python manage.py startapp crudapp
    * crudapp 앱 생성
    * ![startapp](https://user-images.githubusercontent.com/72541544/115647751-55b3cf00-a35f-11eb-9b98-7ccb1a58a74c.png)
* project와 app 이어주기
  * INSTALLED_APPS = [~]에 'crudapp.apps.CrudappConfig', 를 추가해준다.
  * ![setting](https://user-images.githubusercontent.com/72541544/115647763-58162900-a35f-11eb-9315-10b8e5e63270.png)
* app에 templates 폴더 추가, 폴더 안에 home.html 만들기
  * 이때, MTV 패턴 중 T, Template 폴더가 생성되며 안에는 html이 들어간다. 
  * ![template](https://user-images.githubusercontent.com/72541544/115647752-564c6580-a35f-11eb-87d4-e1742785d8b2.png)
* view.py에 home란 이름의 함수 만들기
  * View를 메서드로 구현한 것이 view.py이며 웹이나 Database에서 온 요청을 처리한다.
  * home는 요청이 들어오면 home.html을 실행
  * ![viewpy](https://user-images.githubusercontent.com/72541544/115647756-56e4fc00-a35f-11eb-9849-57929827b8fa.png)
* project의 urls.py와 app의 views.py 연결하기
  * from crudapp import views
  * path(' ',views.home, name='home'),
    * 이때 템플릿 처리를 한 후 html로 된 응답 데이터를 웹 클라이언트로 반환한다.
  * app과 project는 다른 디렉터리에 있어 서로 연결한다.
  * ![urlspy](https://user-images.githubusercontent.com/72541544/115647755-564c6580-a35f-11eb-8ecd-b8474e975e01.png)
* 이제 입력한 내용들을 확인하기 위해 python manage.py runserver 입력한다.
  *  http://127.0.0.1:8000/ 클릭시 출력내용 확인가능
  * ![runserver2](https://user-images.githubusercontent.com/72541544/115647761-58162900-a35f-11eb-94e4-65798a70f391.png)
* 결과
  * ![result](https://user-images.githubusercontent.com/72541544/115647759-577d9280-a35f-11eb-8f92-b87b9a363f20.png)
* 지금까지 한 내용은 MVT 패턴 중 View, Template을 사용하였다.
* View 같은 경우, views.py 메서드로 구현되며 웹이나 Database에서 온 요청을 처리한다.
  * 최종으로 데이터를 html로 변환하기 위해 Template 처리를 한 후 html로 응답 데이터를 웹 클라이언트로 반환한다.
* Template은 html 파일들이 저장된 디렉터리이다.



* runserver 나가기 : ctrl + c



# 시작하기에 앞서

* 가장 먼저 해야할 것
  * 현재 myvenv 디렉터리 메모리가 매우 커 git디렉터리 밖에 나두었다.
  * 현재 디렉터리 경로에서 cd를 이용하여 myvenv가 있는 디렉터리(한 칸위 디렉터리로) 이동한 후
  * source myvenv/Scripts/activate를 입력하여 가상머신을 실행한 후
  * 다시 project가 있는 디렉터리로 돌아와 
  * python manage.py runserver를 입력하면 실행이 된다.

# Django 모델링

* project 디렉터리에서

  * __init__.py
    * package임을 알려주는 모듈
  * setting.py
    * Django의 설정을 담당하는 부분
    * 가장 중요한 것
      * 현재 최상위 디렉터리(프로젝트) -> 현재 최상위 디렉터리(프로젝트)-> setting.py
      * INSTALLED_APPS에 현재 crudapp이 설치되었다는 것을 알려줘야 한다.
      * ![INSTALLED_APPS](https://user-images.githubusercontent.com/72541544/115669143-ec45b780-a382-11eb-98cd-b9664395f6cc.png)
  * urls.py
    * app 경로설정
  * wsgi.py
    * webserver 게이트웨이 인터페이스, 배포할 때 파이프라인 연결하는 구간
  * manage.py
    * 다양한 명령어가 저장되어 있는 곳 

* 모델링을 통한 테이블 생성

  * models.py에서 모델링을 한다.
  * python manage.py makemigrations로 주문서를 만든다.
  * python manage.py migrate로 주문서 내역대로 테이블을 생성한다.

* app 생성

  * 최상위 프로젝트에서 python manage.py startapp app이름
    * 이렇게 할시, app이 만들어지고 안에는 밑과 같이 py가 생성됨
    * ![startappname](https://user-images.githubusercontent.com/72541544/115669156-eea81180-a382-11eb-8269-b3ccc3da9af4.png)

* app 디렉터리

  * admin.py : 관리자 페이지 설정 관련 모듈

  * views.py : request를 처리해서 response를 내놓은 곳

  * models.py : 모델을 표현하는 곳이다.

    * ![Postclass](https://user-images.githubusercontent.com/72541544/115669154-eea81180-a382-11eb-9bf7-c75a3245f052.png)

    * ```python
      from django.db import models
      
      
      \# Create your models here.
      
      
      class Post(models.Model): # 모델 상속
      
        title = models.CharField(max_length=200)
      
        \# CharField() : 문자열 데이터 타입
      
        \# max_length : 최대 길이
      
        content = models.TextField()
      
        \# TextField : 1000자 정도의 문자열 데이터 타입
      
        view_count = models.IntegerField(default=0)
      
        \# IntegerField = 정수형 데이터 타입
      
        \# default : 기본값 (초기화 값)
      
      
      
        \# DateTimeField : 시간 날짜 데이터 타입
      
        \# auto_now_add : 생성될 때 현재시간 저장
      
        \# auto_now : 생성, 수정될 때 현재시간 저장
      
        create_at = models.DateTimeField(auto_now_add=True) # 언제 생성
      
        update_at = models.DateTimeField(auto_now=True) # 언제 업데이트 되었는지
      ```

    * 현재 최상위 project 밑 setting에서 app 설정을 완료한 상태라면 실행시, model이 생성된다.

    * python manage.py makemigrations로 주문서를 만든다.

    * ![app 생성](https://user-images.githubusercontent.com/72541544/115669138-ebad2100-a382-11eb-8894-f6e6aab8e13d.png)

    * ![migration생성](https://user-images.githubusercontent.com/72541544/115669148-ed76e480-a382-11eb-847b-4f78f082efb8.png)

    * ![migration init](https://user-images.githubusercontent.com/72541544/115669144-ecde4e00-a382-11eb-88d1-cabd16af3b28.png)

    * id : 기본키(primary key), 고유 식별 가능한 정보

      * 한 table 안에 동일한 id (primary key)를 갖는 객체는 없어야 한다.

    * title, content, view_count, create_at, update_at은 models.py에서 입력한 것

    *  python manage.py migrate : DB에 테이블 형태로 Post을 만든다.

    * python manage.py migrate로 주문서 내역대로 테이블을 생성한다.

    * ![주문서](https://user-images.githubusercontent.com/72541544/115669159-ef40a800-a382-11eb-8b8f-25cff1983658.png)

    * ``` database
      python manage.py shell : shell에 진입한다.(이후)
      * shell에서 객체 생성 및 조회할 수 있다.
      
      from crudapp.models import Post   
      * crudapp : app 이름, Post : DB에 생성한 Table 이름
      
      Post.objects.create(title="간장게장 담그는 법",content="알이 꽉찬 꽃게")
      * ORM, 이를 통해 SQL과 소통을 한다.
      
      Post.objects.all() : 모든 host 테이블 안에 있는 객체들을 불러온다.
      
      # ORM을 통해 조금 전 생성한 id = 1을 갖는 객체를 변수에 담아 속성들을 출력해보기
      post = Post.objects.get(id=1)
      - Post object들 중에서 id를 1로 갖는 object를 post에 저장한다.
      post.title
      - post의 title을 호출한다.
      post.content
      - post의 content을 호출한다.
      post.view_count
      - post의 view_count을 호출한다.
      post.create_at
      - post의 create_at을 호출한다.(생성된 날짜가 출력된다.)
      exit()
      - 쉘에서 나올 때 사용
      ```

    * ![post create](https://user-images.githubusercontent.com/72541544/115669149-ed76e480-a382-11eb-8d04-7a4767333377.png)

      * <Post: Post object (1)> : 1이라는 id 값을 갖는 게시글의 객체라는 뜻이다.

    * ![Post object 조회](https://user-images.githubusercontent.com/72541544/115669150-ee0f7b00-a382-11eb-8ab6-4e584d55e7da.png)
      * Post.objects.all() : 모든 host 테이블 안에 있는 객체들을 불러온다.
      * <QuerySet [<Post: Post object (1)>]> : QuerySet Box안에서 Post 객체 첫 번째 값을 불러온다.


# 관리자 페이지 활용

* Django에서는 관리자 페이지를 쉽게 만들 수 있다.

* 저번 수업때 배운 것

  * python manage.py makemigrations
    * 테이블을 생성하기 위한 주문서 만듦(생성)
  * python manage.py migrate
    * 주문서 내역대로 테이블 생성
  * python manage.py shell
    * 만든 테이블 확인, 생성, 조회

* 'crudapp' 앱 (폴더) 안의 admin.py에서 table에서 관리자 페이지 확인

* 관리자 페이지에 접근하기 위해서는 UserID가 있어야한다.

* User을 생성한다.

* python manage.py createsuperuser

* ![SuperUser  생성](https://user-images.githubusercontent.com/72541544/115699599-bdd6d500-a3a0-11eb-823e-05cf1896aceb.png)

* 가상장치를 실행시킨 후 project 디렉터리에 들어와서 runserver를 실행시켜준다.

* ![runserver 실행](https://user-images.githubusercontent.com/72541544/115699598-bdd6d500-a3a0-11eb-8717-157435d019b1.png)

* 다음 127.0.0.1:8000에서 /admin/을 추가한 후 해당 name과 password로 로그인한다.

* ![admin](https://user-images.githubusercontent.com/72541544/115699601-be6f6b80-a3a0-11eb-8584-5451c1e9af79.png)

* Django는 이미 CRUD가 구성되어 있다.

* ![CRUD](https://user-images.githubusercontent.com/72541544/115699586-bc0d1180-a3a0-11eb-8cc8-1ee233cc862c.png)

* 만든 모델들은 admin에서 관리를 한다.

* 이제 admin.py 소스를 입력한다.

* ```python
  from django.contrib import admin
  from django.contrib.admin.options import ModelAdmin
  from .models import Post
  # Post를 가져온다.
  
  # .models: 같은 경로에 있으면 .으로 처리
  
  # # Register your models here.
  # admin.site.register(Post)
  # # 화면에 Post 띄우기
  
  
  # 데코레이터 : 함수나 클래스를 꾸며주는 역할
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
  
      list_display = (
          'id',
          'title',
          'view_count',
          'create_at',
          'update_at'
      )
      # list_display : 원하는 컬럼들을 보여준다.
  
      search_fields = (
          'title',
      )
      # search_fields : 검색이 가능한 컬럼 설정, 항상 ','를 붙여야 한다.
  
      # list_filter, list_display_links 알아보기
  
  ```

* 입력 후 확인 결과

* ![Django administration](https://user-images.githubusercontent.com/72541544/115699596-bd3e3e80-a3a0-11eb-8bac-d1d1d23b48a8.png)

* ![Django admin](https://user-images.githubusercontent.com/72541544/115699593-bd3e3e80-a3a0-11eb-9d8b-cdddcbb1dd1a.png)

* 현재 데코레이터로 함수, 클래스를 꾸며준 후 결과이다.

* admin에서는 CRUD를 관리하기 때문에, 해당 APP에서 POST를 추가할 수 있다.

* 또한, 입력한 list_display, search_fields를 통해 컬럼들을 보여주며, 검색이 가능하다.

* list_filter, list_display_links 및 list관련 변수에 대해 알아봐야 한다.



#### 웹 관련 Django는 여기까지
#### 애플리케이션으로
* Web과 app에서의 Django
![django Rest api1](https://user-images.githubusercontent.com/72541544/115875396-20eb6900-a480-11eb-8c98-b6fe4131ec32.png)




# REST API

* Representational State Transfer
* REST란?
  * http의 url 과 http method(GET, POST, PUT, DELETE)를 사용해서 API 가독성을 높인 구조화된 시스템 아키텍쳐(framework)라고 생각하면 된다.
  * 하나의 URL로 최소 4가지의 HTTP method를 전송할 수 있다.
  * 스마트폰 등장으로 웹으로만 서비스를 제공하는 것에 한계가 있어 등장하게 되었다.
  * JSON, XML 등과 같은 형식을 통해서 데이터를 다루는 별도의 API 서버를 담당한다.
  * Restful 아키텍처를 HTTP Method와 함께 사용해 웹, 데스크탑 앱, 스마트폰 어플들까지 하나의 API 서버를 생성할 수 있다.
  * View 클래스 자체가 RESTful 한 서버를 만들기에 최적화된 framework이다.
* DRF(Django Rest Framework)
  * Django 안에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리이다.
  * Serializer
    * 직렬화된 클래스로서, 사용자의 DB안에 사용자 프로필 사진, 이메일, 이름, 성별이 있다고 가정하면 사용자 모델 인스턴스를 JSON 형태 또는 Dictionary 형태로 직렬화 할 수 있다.
    * ex)로 아래와 같은 User가 있다고 가정한다.
    * DRF의 serializer를 통해 모델 인스턴스를 직렬화 할 수 있다.
    * ![DRF serializer](https://user-images.githubusercontent.com/72541544/115875378-1d57e200-a480-11eb-8d40-b066162373aa.png)
    * 사용자 정보를 열람하는 URL : /serializer/user/<user id>/
    * View에서는 user_id의 해당하는 모델 인스턴스의 정보를 리턴한다.
    * 이럴 경우, /serializer/user/1/이라는 URL로 요청했을 때, user_id가 1인 사용자의 정보를 JSON 형태로 응답받을 수 있다.
    * 정리하자면, 사용자 프로필 페이지에 접근했을 때 사용하는 View라고 하면, 사용자 페이지에 들어갈 때마다 해당하는 사용자의 user_id만 URL에 입력하게되면 각 사용자의 정보를 JSON 형태로 응답 받을 수 있다.
    * 이러한 기능을 하는 Serializer를 ModelSerializer이라고 부른다.
  * DRF 실제 설치
    * pip install djangorestframework
    * ![djangorestframework 설치](https://user-images.githubusercontent.com/72541544/115875374-1c26b500-a480-11eb-851e-d0b04c8cb24a.png)
    * rest framework 추가
    * ![rest framework app 추가](https://user-images.githubusercontent.com/72541544/115875379-1d57e200-a480-11eb-99ff-0f3dc3757886.png)



* Moblie, Django?
  * 모바일에서 장고를 사용하는 이유는
    * 프론트엔드와 백엔드간의 REST 기반의 통신 아키텍처로 완전한 Decoupling을 용이하게 할 수 있어 사용한다.
    * Decoupling : app을 다시 배치하지 않고도 parameters(매개 변수)를 변경할 수 있게 설정을 구성해준다. 
  * ![django json api](https://user-images.githubusercontent.com/72541544/115875385-1e890f00-a480-11eb-9627-b33cc0e0269b.png)
    * 안드로이드에서는 Http API를 요청하고, Backend에서는 Json으로 응답한다.
    * Android에서는 Component Renderer, View Controller가 필요하고
    * BackEnd에서는 API View, ORM, Serializer이 필요하다. 



# 실습

```bash
- django-admin startproject studyrestframework
: 프로젝트 생성
- cd studyrestframework/
: 프로젝트 디렉터리로 이동
- pip install djangorestframework
: djangorestframework 설치(안드로이드와 연동할 때 사용)
- python manage.py migrate
: migrations(이동, 이주)를 적용 또는 취소, DB를 초기화
- python manage.py createsuperuser
: 슈퍼 유저 만듦
- python manage.py showmigrations
: 현재 상황을 추척

```

### Serializer 생성

* JSON, XML 파일등으로 바꾸어 준다.

```python
# crudproject/phoneapp/seralizer.py

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # HyperlinkedModelSerializer
    class Meta:
        model = Group
        fields = ('url', 'name')

```

* HyperlinkedModelSerializer이외 다른 것을 사용할 수 있지만, hyperlink를 하는게 좋은 RESTful 디자인이다.

### Views.py

```python
# crudproject/phoneapp/views.py
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from phoneapp.seralizer import UserSerializer, GroupSerializer

# project 경로 설정할 필요 없다.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

```

* viewsets : view들을 결합
  * 여러 가지 API 기능을 통합해서 하나의 API Set로 제공하는 것
  * 하나의 Model을 가지고 list, detail 등 각각의 API를 만들어 보면, 중복되는 로직이 많다.
    * 이럴 때, ViewSet을 쓰게 되면 중복되는 로직의 코드를 줄일 수 있어 코드의 효율성을 높일 수 있다.
  * list(), create() 액션을 제공
  * Viewsets을 위한 method 핸들러들은 as_view()함수를 사용해 view가 끝나는 시점에 해당하는 행동을 취할 때 바인딩한다.
  * 일반적으로 url 설정 내에서 viewset들의 view를 명시적으로 하는 것보다 router클래스로 viewset을 등록하는 것이 좋다.

### urls.py

```python
# crudproject/crudproject/urls.py

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from phoneapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

```

* view대신 viewset을 사용해서 자동적으로 URLconf를 우리의 API에 생성
* router클래스에 등록해주기만 하면 된다.
* API, URL들을 기본 제공하는 기능에서 추가하고 싶을 때 URLconf를 명시해주면 된다.
  * URLconf : url 요청이 들어오면 어떤 views.py의 함수를 실행시킬지 정희하는 단계
  * __path('클라이언트로 받는 요청 URL', views.py에 정의되어있는 함수)__
  * 해당 프로젝트 app 마다 urls.py를 생성 후 각각 관리하기가 매우 좋은 방법
  * Django는 기본적으로 라우팅을 위해 urls.py를 찾을 때 프로젝트 디렉터리 안에 있는 urls.py를 찾는다.
    * 이때, include을 사용한다.
    * path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
      * include를 사용 위치경로 설정, rest_framework 하위의 urls.py 파일을 찾아 실행한다. namespace는 rest_framework로 되어 있다.

### # settings.py

```python
# crudproject/crudproject/settings.py

INSTALLED_APPS = [
    ~
    'rest_framework',   # 추가
]


~

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### 실행 및 결과

```bash
python manage.py runserver
```

![Api Root](https://user-images.githubusercontent.com/72541544/115875382-1df07880-a480-11eb-82ad-716354b4ac2b.png)








[참고 자료] : https://jong-seok-ap.tistory.com/32

[참고 자료] : https://butter-shower.tistory.com/50

[참고 자료] : https://butter-shower.tistory.com/52

[참고 자료] : https://m.blog.naver.com/complusblog/221177123238

[참고 자료] : https://integer-ji.tistory.com/82?category=745989



