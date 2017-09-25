settings

1. djangogirls 폴더 생성
   projects
     django
       djangogirls
         .git
         .gitignore
         .python-version
         requirement.txt
2. git init
3. gitignore 작성
 3-1. gitignore내부에 .idea/ 추가
4. pyenv virtualenv fc-djangogirls생성
5. pyenv local fc-djangogirls
6. GitHub new repository: Djangogilrls
7. local Git에 GitHub remote 저장소 추가
8. pycharm 해당 프로젝트 폴더 open 후 interpreter 설치 
   [file]-[settings]-[interpreter]:  ~/.pyenv/versions/fc-djangogirls/bin/python
9. pip install django
10. requirement.txt
   pip freeze >> requirement.txt
11. pip 환경
   ~/.pip/pip.conf
   [list]
   format=columns