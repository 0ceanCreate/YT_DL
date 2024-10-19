import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

audio_options = []  # Lista para armazenar as qualidades de áudio disponíveis

# Função para verificar as qualidades de áudio disponíveis
def verificar_audio_qualidade():
    global audio_options  # Usar a variável global para armazenar as opções de áudio
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
        return

    # Opções do yt-dlp para listar os streams de áudio
    ydl_opts = {
        'quiet': True,  # Suprimir a saída normal do yt-dlp
        'format': 'bestaudio/best',  # Listar apenas os streams de áudio
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])

            audio_options = [f for f in formats if f.get('vcodec') == 'none']  # Somente streams de áudio

            if not audio_options:
                messagebox.showwarning("Aviso", "Nenhuma qualidade de áudio disponível para este vídeo.")
                return

            # Limpar os Radio Buttons anteriores
            for widget in audio_frame.winfo_children():
                widget.destroy()

            # Criar Radio Buttons para cada qualidade de áudio disponível
            for audio in audio_options:
                bitrate = audio.get('abr') or 'Desconhecida'
                label = f'{bitrate} kbps'
                tk.Radiobutton(audio_frame, text=label, variable=selected_audio, value=audio['format_id']).pack()

            messagebox.showinfo("Informação", "Qualidades de áudio encontradas! Selecione uma opção.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao verificar a qualidade de áudio: {e}")

# Função para baixar o áudio na qualidade selecionada
def baixar_audio():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
        return

    if not selected_audio.get():
        messagebox.showerror("Erro", "Por favor, selecione a qualidade de áudio.")
        return

    # Abrir o diálogo para selecionar o diretório de salvamento
    pasta_destino = filedialog.askdirectory()

    if not pasta_destino:
        messagebox.showerror("Erro", "Nenhum diretório selecionado.")
        return

    # Opções do yt-dlp para baixar o áudio na qualidade selecionada e converter para MP3
    ydl_opts = {
        'format': selected_audio.get(),  # Qualidade de áudio selecionada
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Converter para MP3
            'preferredquality': '192',  # Qualidade do MP3 (padrão 192 kbps)
        }],
        'progress_hooks': [progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o áudio: {e}")

# Função para baixar o vídeo na resolução selecionada
def baixar_video():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
        return

    # Abrir o diálogo para selecionar o diretório de salvamento
    pasta_destino = filedialog.askdirectory()

    if not pasta_destino:
        messagebox.showerror("Erro", "Nenhum diretório selecionado.")
        return

    # Escolha de resolução
    opcao_escolhida = selected_video_res.get()

    # Opções do yt-dlp para baixar apenas o vídeo (com áudio) e converter para MP4 se necessário
    ydl_opts = {
        'format': f'bestvideo[height<={opcao_escolhida}]+bestaudio/best[height<={opcao_escolhida}]',
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  # Garantir que o arquivo final seja em MP4
        'progress_hooks': [progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")

# Função para exibir o progresso do download
def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')  # Tamanho total do arquivo
        downloaded_bytes = d.get('downloaded_bytes', 0)  # Tamanho baixado até agora
        
        if total_bytes:
            percent = downloaded_bytes / total_bytes * 100
            progress_label.config(text=f"Progresso: {percent:.2f}%")
            root.update_idletasks()
    elif d['status'] == 'finished':
        progress_label.config(text="Download concluído!")
        messagebox.showinfo("Sucesso", "Download concluído!")

# Criar a janela principal
root = tk.Tk()
root.title("Downloader de Vídeos e Áudio do YouTube (yt-dlp)")

# Entrada de URL
url_label = tk.Label(root, text="URL do Vídeo:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10)

# Frame para os Radio Buttons das qualidades de áudio
audio_frame = tk.Frame(root)
audio_frame.pack(pady=10)

# Variável para armazenar a opção de áudio selecionada
selected_audio = tk.StringVar()

# Variável para armazenar a opção de resolução de vídeo
selected_video_res = tk.StringVar(value="720")  # Resolução padrão

# Radio Buttons para as resoluções de vídeo
res_label = tk.Label(root, text="Escolha a resolução de vídeo:")
res_label.pack(pady=10)

resolucoes = ["360", "480", "720", "1080", "1440", "2160"]

for res in resolucoes:
    tk.Radiobutton(root, text=f'{res}p', variable=selected_video_res, value=res).pack()

# Botão para verificar as qualidades de áudio disponíveis
verificar_audio_button = tk.Button(root, text="Verificar Qualidades de Áudio", command=verificar_audio_qualidade)
verificar_audio_button.pack(pady=10)

# Botão para baixar o áudio na qualidade selecionada
baixar_audio_button = tk.Button(root, text="Baixar Áudio (MP3)", command=baixar_audio)
baixar_audio_button.pack(pady=10)

# Botão para baixar o vídeo na resolução selecionada
baixar_video_button = tk.Button(root, text="Baixar Vídeo", command=baixar_video)
baixar_video_button.pack(pady=10)

# Label de progresso
progress_label = tk.Label(root, text="Progresso: 0%")
progress_label.pack(pady=10)

# Executar a interface
root.mainloop()
