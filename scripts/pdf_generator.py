import sys
import subprocess
import base64
import os

def generate_pdf(html_content):
    """
    Converts HTML string to PDF using wkhtmltopdf and returns base64.
    """
    html_path = "/tmp/input.html"
    pdf_path = "/tmp/output.pdf"

    try:
        # 1. Escreve o arquivo de forma segura (evita injeção via shell)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 2. Executa o wkhtmltopdf sem usar shell=True por segurança
        subprocess.run(["wkhtmltopdf", "--quiet", html_path, pdf_path], check=True)

        # 3. Lê o PDF e converte para base64
        with open(pdf_path, "rb") as f:
            pdf_base64 = base64.b64encode(f.read()).decode('utf-8')
            print(pdf_base64)

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    finally:
        # Cleanup
        for path in [html_path, pdf_path]:
            if os.path.exists(path):
                os.remove(path)

if __name__ == "__main__":
    # Lê o HTML do stdin (entrada padrão) para evitar problemas com tamanho de argumento
    input_html = sys.stdin.read()
    if input_html:
        generate_pdf(input_html)
