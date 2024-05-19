import os
import tkinter as tk
from tkinter import filedialog, messagebox
from dbconnector import fetch_data
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def create_pdf(data, pdf_file):
    document = SimpleDocTemplate(pdf_file, pagesize=A4)

    # フォントのディレクトリ指定
    font_dir = os.path.join(os.path.dirname(__file__), 'fonts')
    font_path = os.path.join(font_dir, 'NotoSansJP-Regular.ttf')

    # フォントファイルの存在を確認
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")

    # 日本語フォントの登録
    pdfmetrics.registerFont(TTFont('NotoSansJP', font_path))

    # スタイルシートを取得し、日本語対応のスタイルを追加
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontName='NotoSansJP',
        fontSize=18,
        leading=22,
        textColor=colors.black,
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['BodyText'],
        fontName='NotoSansJP',
        fontSize=10,
        leading=12,
        textColor=colors.black,
    )

    title = Paragraph("テーブルタイトル", title_style)
    spacer = Spacer(1, 12)  # スペーサーを追加
    
    subtitle = Paragraph("テーブル2", title_style)

    # データのヘッダー（日本語）
    headers = ["id", "名前", "性別", "年齢"]
    data.insert(0, headers)

    # 日本語対応のスタイルを各セルに適用
    styled_data = []
    for row in data:
        styled_row = []
        for item in row:
            styled_item = Paragraph(str(item), body_style)
            styled_row.append(styled_item)
        styled_data.append(styled_row)

    table = Table(styled_data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'NotoSansJP'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # 要素のリストを作成
    elements = [title, spacer, subtitle, spacer, table]
    document.build(elements)

def save_pdf():
    data = fetch_data()
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if save_path:
        try:
            create_pdf(data, save_path)
            messagebox.showinfo("完了", "PDFファイルが正常に保存されました")
        except Exception as e:
            messagebox.showerror("エラー", f"PDFファイルの生成中にエラーが発生しました: {str(e)}")

def main():
    root = tk.Tk()
    root.title("PDF生成アプリケーション")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="PDFを生成して保存するには、以下のボタンをクリックしてください。")
    label.pack(pady=5)

    button = tk.Button(frame, text="PDFを生成", command=save_pdf)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
