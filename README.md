## Table of Contents
- [Movie Filming Location Web Application, Fillow](#movie-filming-location-web-application-fillow)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Recent Updates](#recent-updates)
  - [](#)
  - [Projet Restrospective](#projet-restrospective)
  - [`영화 추천 알고리즘에 대한 기술적 설명`](#영화-추천-알고리즘에-대한-기술적-설명)
  - [License](#license)

# Movie Filming Location Web Application, Fillow
`서비스 대표 기능에 대한 설명`

Fillow은 사용자들이 영화 촬영 장소를 탐색하고 해당 영화 장면을 유튜브로 볼 수 있는 Vue 웹 애플리케이션입니다. MovieList, MovieVideo, MovieDetail 및 MapView를 비롯한 여러 구성 요소로 구성됩니다.

## Features
- MovieList: 기본 정보가 포함된 동영상 목록을 표시합니다. 사용자는 목록을 스크롤하여 관심 있는 영화를 찾을 수 있습니다.
- MovieVideo: 선택한 동영상과 관련된 YouTube 동영상을 표시합니다. 사용자는 애플리케이션 내에서 직접 동영상을 볼 수 있습니다.
- MovieDetail: 제목, 릴리스 날짜, 출연자 및 스토리라인을 포함하여 선택한 동영상에 대한 자세한 정보를 제공합니다.
- MapView: Google 지도 API와 통합하여 동영상 촬영 위치를 나타내는 마커가 있는 지도를 표시합니다. 사용자는 마커를 클릭하여 촬영 위치에 대한 추가 정보를 볼 수 있습니다.

## Project Structure
```
|- components/
  |- InfoWindow.vue
  |- MovieDetail.vue
  |- MovieInfo.vue
  |- MovieList.vue
  |- MovieListItem.vue
  |- MovieVideo.vue
  |- RecommendItem.vue
|- views/
  |- AddMovieView.vue
  |- ChangePassWordView.vue
  |- LoginView.vue
  |- MapView.vue
  |- MyMapView.vue
  |- RecommendView.vue
  |- SignUpView.vue
|- router/
  |- index.js
|- assets/
  |- images/
|- App.vue
|- main.js
```
- components: a
- views: app 내 전체 페이지
- router: 서로 다른 view 간에 이동 할 수 있도록 Vue Router를 구성
- app.vue: 응용 프로그램의 진입점 역할을 하는 루트 Vue 구성 요소
- main.js: Vue app을 초기화하고 DOM에 마운트한다.

---
## Recent Updates
  주요 성취 사항, 해결한 버그와 문제에 대한 설명과 해당 수정 내용을 기록합니다.
<details>
  <summary>5/16/2023 - Vue 프로젝트 생성, 홈 화면 기획</summary>

  `BACK`
  -  `vue create fillow`로 vue 프로젝트 생성
  - `$vue add vuex`
  - `npm i vuex-persistedstate`

  - Google Cloud Platform에서 구글 API 키 생성하기
    - Google Cloud Console에 로그인한 다음 새 프로젝트를 만들기.
    - Google Cloud Console의 ‘API 및 서비스’ 메뉴를 선택하여, ‘API 및 서비스 라이브러리’를 선택
    - ‘API 라이브러리’ 페이지에서 ‘Maps JavaScript API’를 검색하고 선택
    - ‘API 키 이름’을 지정하고, 키 생성
    - front-pjt-front/fillow 경로 하위에 `.env.local` 파일을 만들고 VUE_APP_GOOGLE_MAP_API_KEY 에 API KEY 값을 넣어 사용할 준비 마치기
    - API 키 제한하기 키를 localhost로 제한하여 익명의 의도치 않은 트래픽을 차단하고 API 호출 회수 수를 제한

  `FRONT`
  ![홈 화면 기획](https://file.notion.so/f/s/509d37dd-644d-4a15-a148-6cf2f5dbb342/Untitled.png?id=e9f338c5-404c-477d-b9e3-86641bf8c808&table=block&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&expirationTimestamp=1685082892960&signature=_K0o8Bir01pybRxep44-h-dfACcK7KK8tDhLLOi7KnY&downloadName=Untitled.png)
</details>

<br>

<details>
  <summary>5/17/2023 - 초기 데이터 생성</summary>

  ![초기 데이터](https://file.notion.so/f/s/097402aa-d31d-4be7-9f98-461b1ddc321c/Untitled.png?id=b3c7cc46-74ef-4d96-9316-0628cab8e293&table=block&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&expirationTimestamp=1685083722741&signature=TrzMw-Twboji0vUL0-qzeE-SCvWFvEbREG10umKSVz4&downloadName=Untitled.png)
  - 영화 TMDB ID와 영화장소 데이터 정보가 결합된 데이터 객체 50개 만들기
</details>

<br>

<details>
  <summary>5/18/2023 - DB Model 정의, TMDB API로 데이터 가져오기</summary>

  `BACK`
  - DB model 정의하고, Post맨을 이용하여 응답이 들어오는지 테스트 
  - 로그인, 로그아웃 테스트
  
  `FRONT`
  - TMDB로 영화 상세 정보 보여줄 수 있도록 데이터 가져오기 (get('https://api.themoviedb.org/3/movie/popular?language=ko-KR'))
  - 영화 관련 유튜브 동영상 보여주기 ( iframe 사용 )
</details>

<br>

<details>
  <summary>5/19/2023 - 장고 영화, 지역 CRUD 기능 구현</summary>

  `BACK`
  - 사용자가 직접 TMDB ID, 영화 장소 정보를 Create, Update 수 있게 하기
  - api를 이용해 요청받은 json데이터를 저장하기 위해 장고 querydict형태로 다시 변환
  - 다대다 관계 create시 FK를 가지는 특정 필드를 제외한 시리얼라이저를 사용후 장고 다대다 object manager에 add를 이용해 강제적으로 추가
  - serializer을 이용해 json으로 응답할 수 있도록 설정, 화면 구현하는데 필요한 데이터들 대부분 정의 완료
  - 로그인, 로그아웃 등 인증 시스템 구현
  - postman을 이용해 응답 확인
  - 미리 준비한 데이터 장고 loaddata 받을 수 있도록 json화 시켜서 저장
  - 미리 준비한 데이터와 일치하는 영화 데이터를 tmdb api를 이용해 받아온 후 마찬가지로 json화 시켜서 저장
  - 데이터 DB저장 확인

  `FRONT`
  ![데이터 확인](https://file.notion.so/f/s/c137338c-2386-4618-887a-aeb3f65af5e3/Untitled.png?id=d0ebdaad-ffab-48e5-9486-7bd0603f4f81&table=block&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&expirationTimestamp=1685088190481&signature=QyBZuZ1rvMro4Meo5XcAz1u6svIhXzUKa6oDuXfSqPg&downloadName=Untitled.png)
  - 필요한 컴포넌트들 정의 및 데이터 확인
  - 각 컴포넌트들을 생성 후 관계 설정
  - 컴포넌트별로 필요한 데이터 이동시키는 작업
</details>

<br>

<details>
  <summary>5/20/2023 - Google Map, TMDB 데이터 확인</summary>

  `BACK`
  - 영화 촬영지의 위도, 경도 정보를 토대로 구글 맵에 마커로 띄우고, 마커를 클릭했을때 해당 영화에 대한 추가 정보를 볼 수 있도록 하는 기능 구현
  1) 구글 맵 설치: npm install vue2-google-maps

  `FRONT`
  ![데이터확인](https://file.notion.so/f/s/df4a89af-d725-4fab-8168-31225a8a5a17/Untitled.png?id=0b8f9076-30aa-4e6e-8262-f522b8783174&table=block&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&expirationTimestamp=1685084987500&signature=XZ5nUXJdqpuFE4p6uJIITPRWS3MssOjEkZ1nWpnoBeA&downloadName=Untitled.png)

</details>

<br>

<details>
  <summary>5/22/2023 - 페이지네이션 구현, 모델 소폭 수정</summary>

  `BACK`
  - 페이지네이션을 이용해 일부 데이터만 요청 받을 수 있도록 location 테이블과 user 테이블 연결, movie table 필드 추가

  `FRONT`
  ![진행상황](https://file.notion.so/f/s/df4a89af-d725-4fab-8168-31225a8a5a17/Untitled.png?id=0b8f9076-30aa-4e6e-8262-f522b8783174&table=block&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&expirationTimestamp=1685084987500&signature=XZ5nUXJdqpuFE4p6uJIITPRWS3MssOjEkZ1nWpnoBeA&downloadName=Untitled.png)
  - HEADER 구현

</details>

<br>

<details>
  <summary>5/23/2023 - 쿼리문을 통한 movie list 검색 가능하도록 구현, 페이지네이션, 추천 기능 구현</summary>

  `BACK`
  - 장고 Q 객체 이용, 프론트에서 받아온 쿼리문을 이용한 간단한 검색 기능
  - 영화 추천 기능 구현
    - 자신의 위치 데이터를 받아옴
    - 자신의 위치 데이터를 기준으로 DB에 저장된 모든 location과 물리적 거리 비교
    - 가장 가까운 장소를 가진 영화 몇가지를 추천
    - 생성된 페이지에 데이터 옮겨놓는 작업
    - 요청받은 장소 데이터의 좌표를 이용해 지도의 focus를 옮길 수 있도록 구현

  `FRONT`
  - 데이터 추가시 화면 상의 변화가 없던 점 수정
  - emit 이벤트를 이용해 데이터의 변화를 알림, 다시 DB로 데이터 요청해 화면 구현
  - 프론트에서 무한 스크롤 페이지네이션 가능하도록 구현
  - 검색 기능 구현, 쿼리문 별로 요청을 제대로 보낼 수 있도록 처리
  - 추천 페이지 구현 
</details>

<br>

<details>
  <summary>5/24/2023 - 영화, 지역 CRUD 기능 구현, 기타 버그 수정</summary>

  `BACK`
  - 사용자가 직접 TMDB ID, 영화 장소 정보를 Create, Update 수 있게 하기
  - serializer을 이용해 json으로 응답할 수 있도록 설정
  - 로그인, 로그아웃 등 인증 시스템 구현
  - postman을 이용해 응답 확인

  `FRONT`
  - 영화 선택 시 해당 location으로 지도의 focus 이동 할 수 있도록 설정
  - watch를 이용해 데이터 변화를 감지하여 구현
  - 발생하는 예외들 간간히 처리
    - v-for문 키값 기준으로 렌더링, key값에 DB에 저장된 완전 고유한 값 할당하여 해결
    - 데이터 수정, 생성 시 지도가 뜻대로 움직이지 않는 문제는 watch 메서드 수정하여 해결
    - 추천 알고리즘 수정 완료. 
</details>

<br>

<details>
  <summary>5/25/2023 - 기타 버그 수정, 배포</summary>

  `BACK`
  * 시리얼라이저 수정, 페이지네이션 수정, 버그 개선

  `FRONT`
  * 추가적인 css 작업들, 백 변화로 인한 데이터 받는 방식 전환
      ```
</details>

<br>
---
## Projet Restrospective
  `프로젝트 목표와 목적 달성여부`
  - 프로젝트의 목표와 목적을 달성하였습니다.  

  `사용된 기술과 도구의 장점과 한계`
  - Django: serializer와 auth system을 이용하는 과정에서 시행착오가 생겼습니다. 제대로 알고 써야 더 좋은 결과를 가져올 수 있음을 알게 되었습니다.
  - Vue: axios를 이용해 비동기 요청을 보내는 타이밍이 자주 엇갈렸습니다. 그리고 프로젝트를 진행하는 과정에서 불필요한 요청이 자주 발생하였습니다. 처음 설계를 할 때에 관계를 더 잘 잡아야 한다 생각합니다.
  - CSS: 유지보수성을 고려하지 못한 결정은 프로젝트에 부정적인 영향을 미쳤습니다. 예를 들어, scoped 설정을 하지 않은 스타일 코드는 CSS 작성자의 기억력에 의존하여 유지 및 수정이 어려운 상황을 초래했습니다.
  
  `팀원 간의 협업과 커뮤니케이션에 대한 평가`
  - 먼저 프론트엔드와 백엔드 각각의 역할과 책임을 명확하게 정의하였습니다. 프런트엔드 영역은 사용자 인터페이스(UI)와 사용자 경험(UX)에 집중하고, 백엔드 영역은 데이터 처리에 집중했습니다. 프론트엔드와 백엔드 사이의 기능을 분리하여 작업을 진행했습니다.
  - LiveShare Extension으로 팀원과 같은 코드를 보면서 수정함으로써 수월하게 소스 코드의 버전을 관리하였습니다. 필요한 경우 코드의 리뷰를 통해 품질을 검토합니다. 이를 통해 충돌을 방지하고 코드 변경 사항을 추적하였습니다.
  - 인터페이스 정의: 
  - README를 공동으로 작성하였습니다. 
  - 프로젝트의 데드라인을 고려하여 팀원과 협의하여 완성도와 기능성을 균형 있게 조율해야 했습니다.
  
  `개인적인 성장과 학습 경험 (어떤 새로운 스킬이나 지식을 습득했는지)`
  - 위의 방법을 활용하여 각자가 잘하는 분야에 집중하면서도 효과적인 협업을 할 수 있습니다.

  ``
  `영화 데이터 구현`
  - 영화 추천 알고리즘 (어떤 방식으로 추천 시스템을 구현했는지 기술적으로 설명하기, IP 위치 정보 수집 방법)
  
  `데이터베이스 모델링 (ERD)`
  - 유저간 커뮤니티 기능 설명 (어떤 기능이 있는지)
  ![image](https://github.com/pplemover/fillow/assets/122508528/ee6a022c-c653-4c38-a89d-1d64904e0d9a)


  `영화 추천 알고리즘에 대한 기술적 설명`
  - 

  `기타 (느낀 점, 후기 등)`

---
## License
This project is licensed under the MIT License.