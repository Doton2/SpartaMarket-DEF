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
     <details>
     <summary>이미지 </summary>
     <div markdown="1">
         - **Endpoint**: **`/api/accounts`**
         - **Method**: **`POST`**
         - **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능
         - **검증**: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).
         - **구현**: 데이터 검증 후 저장.
         
     
     
     </div>
     </details>
  3. 로그인
  4. 프로필 조회
  5. 상품 등록
  6. 상품 목록 조회
  7. 상품 수정
  8. 상품 삭제


