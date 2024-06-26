import gradio as gr
import pandas as pd

FILE_PATH = "result.xlsx"

def excel_viewer():
    # 지정된 경로의 Excel 파일을 pandas DataFrame으로 읽기
    df = pd.read_excel(FILE_PATH)
    # DataFrame을 HTML 테이블로 변환하여 반환
    return df.to_html()

# Gradio 인터페이스 구성
interface = gr.Interface(
    fn=excel_viewer,  # 파일을 처리할 함수
    inputs=None,  # 입력 없음
    outputs="html",  # HTML 형식의 출력
    title="Excel Viewer",  # 인터페이스 제목
    description="Displaying contents of a predefined Excel file."  # 인터페이스 설명
)

# 인터페이스 실행
if __name__ == "__main__":
    interface.launch()


