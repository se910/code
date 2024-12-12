import streamlit as st

# 타이틀 적용 예시
st.title('암호화 프로그램		:closed_lock_with_key:')

# 캡션 적용
st.caption('20905 김세은')

# divider 삽입
st.divider()

# Subheader 적용
st.subheader('안녕하세요! :sparkles:')
st.markdown("위 웹페이지는,")
st.markdown("암호화 프로그램을 개발하여 **:blue[민감한 데이터를 안전하게 보호하고, 디지털 보안을 강화 ]** 하는 것을 목적으로 시작하였습니다.")


# 빈칸
st.header('')

# Header 적용
st.header('1. 카이사르 암호란?')
st.latex(r'Caesar⠀cipher')
st.write('기원전 100년경에 로마의 장군 **카이사르**가 썼던 암호로, 시저 암호라고도 불립니다.')
st.write("이 암호는 평문에서 사용되고 있는 알파벳을 암호키 **k개만큼 평행이동**시켜 암호화하는 **치환 암호**입니다.")
st.image("3443.jpeg", width = 600 , caption = "평행이동 알고리즘 과정")


# # 빈칸
# st.header('')
# st.header('')
# st.caption('아이폰 사용자일 경우 사용이 제한될 수 있습니다.')

# Header 적용
st.header('')
st.header('')
st.header('2. 카이사르 암호화 프로그램')


ALPHABET = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 
            'L':11, 'M':12, 'N':13, 'O': 14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 
            'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}

key = 3


plain_text = st.text_input("평문을 '영어로' 입력하세요 : ")
plain_text = plain_text.upper()
crypto_text = ""

for p in plain_text :
  if p == " " :
    crypto_text = crypto_text + " "
  else :
    #print(ALPHABET.keys()[ALPHABET.get(p)+3])
    crypto_text = crypto_text + (list(ALPHABET.keys())[ (ALPHABET.get(p)+3)%26 ])
st.write("암호문 :", crypto_text)
