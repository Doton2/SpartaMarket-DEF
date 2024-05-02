# SpartaMarket_DRF


## 주제

기존에 만든 sparta market은 중고거래 중개 사이트의 백앤드 부분만 따로 DRF를 사용해서 작성했다.
회원가입, 로그인, 게시물 등록등의 기능을 Django REST Framework를 통해 API를 JSON형태로 
응답하는 서버를 만들었다.

***

## 개발 기간 
 13.04.24 ~ 16.04.24 개인 일정이있 약 4일간 진행했습니다

***

## 필수 구현 기능 
  1. 회원가입 기능
     - **Endpoint**: **`/api/accounts`**
     - **Method**: **`POST`**
     - **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능
     - **검증**: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).
     - **구현**: 데이터 검증 후 저장.
        <details>
         <summary> 이미지 </summary>
         <div markdown="1">
         <img src= ./img/회원가입.png>
         </div>
        </details>
  3. 로그인
     - **Endpoint**: **`/api/accounts/login`**
     - **Method**: **`POST`**
     - **조건**: 사용자명과 비밀번호 입력 필요.
     - **검증**: 사용자명과 비밀번호가 데이터베이스의 기록과 일치해야 함.
     - **구현**: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지를 반환.
       <details>
        <summary> 이미지 </summary>
        <div markdown="1">
         <img src= ./img/로그인.png>
        </div>
        </details>

  5. 프로필 조회
     - **Endpoint**: **`/api/accounts/<str:username>`**
     - **Method**: **`GET`**
     - **조건**: 로그인 상태 필요.
     - **검증**: 로그인 한 사용자만 프로필 조회 가능
     - **구현**: 로그인한 사용자의 정보를 JSON 형태로 반환.
       <details>
         <summary> 이미지 </summary>
         <div markdown="1">
          왜 안나오냐
          <img src= ./img/로그아웃.png>
         </div>
       </details>
       
  7. 상품 등록
     - **Endpoint**: **`/api/products`**
     - **Method**: **`POST`**
     - **조건**: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.
     - **구현**: 새 게시글 생성 및 데이터베이스 저장.
        <details>
         <summary> 이미지 </summary>
         <div markdown="1">
          <img src= ./img/상품등록.png>
         </div>
        </details>

  9. 상품 목록 조회
      - **Endpoint**: **`/api/products`**
      - **Method**: **`GET`**
      - **조건**: 로그인 상태 불필요.
      - **구현**: 모든 상품 목록 페이지네이션으로 반환.
         <details>
          <summary> 이미지 </summary>
          <div markdown="1">
           <img src= ./img/상품목록조회.png>
          </div>
         </details>
         
  11. 상품 수정
       - **Endpoint**: **`/api/products/<int:productId>`**
       - **Method**: **`PUT`**
       - **조건**: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.
       - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.
       - **구현**: 입력된 정보로 기존 상품 정보를 업데이트.
          <details>
           <summary> 이미지 </summary>
           <div markdown="1">
            <img src= ./img/상품수정.png>
           </div>
          </details>
  13. 상품 삭제
      - **Endpoint**: **`/api/products/<int:productId>`**
      - **Method**: **`DELETE`**
      - **조건**: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.
      - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.
      - **구현**: 해당 상품을 데이터베이스에서 삭제.
         <details>
          <summary> 이미지 </summary>
          <div markdown="1">
           <img src= ./img/상품삭제.png>
          </div>
         </details>

***

## 선택 기능 
  1. 로그아웃
     - **Endpoint**: **`/api/accounts/logout`**
     - **Method**: **`POST`**
     - **조건**: 로그인 상태 필요.
     - **구현**: 토큰 무효화 또는 다른 방법으로 로그아웃 처리 가능.
       <details>
        <summary> 이미지 </summary>
        <div markdown="1">
         <img src= ./img/로그아웃.png>
        </div>
       </details>
  3. 본인 정보 수정
     - **Endpoint**: **`/api/accounts/<str:username>`**
     - **Method**: **`PUT`**
     - **조건**: 이메일, 이름, 닉네임, 생일 입력 필요하며, 성별, 자기소개 생략 가능
     - **검증**: 로그인 한 사용자만 본인 프로필 수정 가능. 수정된 이메일은 기존 다른 사용자의 이메일과 username은 중복되면 안 됨.
     - **구현**: 입력된 정보를 검증 후 데이터베이스를 업데이트.
       <details>
        <summary> 이미지 </summary>
        <div markdown="1">
         <img src= ./img/본인정보수정.png>
        </div>
       </details>

  5. 패스워드 변경
     - **Endpoint**: **`/api/accounts/password`**
     - **Method**: **`PUT`**
     - 조건: 기존 패스워드와 변경할 패스워드는 상이해야 함
     - 검증: 패스워드 규칙 검증
     - 구현: 패스워드 검증 후 데이터베이스에 업데이트.
       <details>
        <summary> 이미지 </summary>
        <div markdown="1">
         <img src= ./img/패스워드변경.png>
        </div>
       </details>
  7. 회원 탈퇴
     - **Endpoint**: **`/api/accounts`**
     - **Method**: **`DELETE`**
     - **조건**: 로그인 상태, 비밀번호 재입력 필요.
     - **검증**: 입력된 비밀번호가 기존 비밀번호와 일치해야 함.
     - **구현**: 비밀번호 확인 후 계정 삭제.
       <details>
        <summary> 이미지 </summary>
        <div markdown="1">
         <img src= ./img/회원탈퇴.png>
        </div>
       </details>


