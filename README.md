# image-resizer
Velog에 포스팅을 올릴 때, 이미지 사이즈를 하나하나 조정하기 귀찮아서 만든 코드입니다.  
예시로 저장해놓은 images 폴더 내 이미지들은 상업적 이용이 가능한 데이터입니다.  

resizing하려는 이미지들을 폴더에 저장한 뒤, 코드를 실행하면 됩니다.  
기본적으로 세로 사이즈를 지정하면, 비율에 맞게 가로 사이즈가 조정되는 방식입니다.  
(is_width_base argument로 가로를 기준으로 resizing할 수 있습니다.)  

개발 과정은 [Velog](https://velog.io/@kyeongjun1007/Velog%EC%97%90-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%98%AC%EB%A6%B4%EB%95%8C%EB%A7%88%EB%8B%A4-%EC%82%AC%EC%9D%B4%EC%A6%88%EB%A5%BC-%EC%A1%B0%EC%A0%95%ED%95%98%EA%B8%B0-%EA%B7%80%EC%B0%AE%EC%9D%84-%EB%95%8C) 포스팅을 참고해주세요.  
<br>  

## Getting Started
```
pip install -r requirements.txt
```

## Example
```bash
python resizer.py --folder_name images --size 500
# 'images' 폴더 내의 이미지들을 세로 500으로 resizing (가로 자동 조정)

python resizer.py --folder_name images --size 1000 --is_width_base
# 'images' 폴더 내의 이미지들을 가로 1000으로 resizing (세로 자동 조정)

```
**arguments**
- folder_name : 이미지를 저장한 폴더 이름
- size : 원하는 출력 이미지의 사이즈
- is_width_base : 가로를 기준으로 resizing (default: False)
