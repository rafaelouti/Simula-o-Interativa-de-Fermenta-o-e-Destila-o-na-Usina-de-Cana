import tkinter as tk
import random

# Configuração da janela principal
root = tk.Tk()
root.title("Simulação de Fermentação e Destilação com Brix e Grau do Álcool (Mais Lento)")
root.geometry("600x550")
root.configure(bg="lightgray")

# Variáveis globais para a fermentação
fermentation_running = False
fermentation_progress = 0
ethanol_amount = 0
initial_brix = 20    # Brix inicial
final_brix = 5       # Brix ao final da fermentação

# Variáveis globais para a destilação
distillation_running = False
distilled_ethanol = 0

# ========================
# FRAME DE FERMENTAÇÃO
# ========================
frame_fermentation = tk.Frame(root, bg="lightgray")
frame_fermentation.pack(fill="both", expand=True)

label_fermentation_title = tk.Label(frame_fermentation, text="Processo de Fermentação", font=("Arial", 16), bg="lightgray")
label_fermentation_title.pack(pady=10)

# Canvas para a fermentação (tanque)
canvas_fermentation = tk.Canvas(frame_fermentation, width=500, height=300, bg="white")
canvas_fermentation.pack(pady=10)

# Desenha o tanque de fermentação (retângulo)
tank = canvas_fermentation.create_rectangle(150, 50, 350, 250, outline="black", width=2)
# Retângulo que representa o nível de fermentação (inicia vazio)
fermentation_fill = canvas_fermentation.create_rectangle(150, 250, 350, 250, fill="green", outline="")

label_fermentation_status = tk.Label(
    frame_fermentation, 
    text="Progresso: 0% | Etanol Produzido: 0 L | Brix: 20",
    font=("Arial", 14), 
    bg="lightgray"
)
label_fermentation_status.pack(pady=5)

def update_fermentation():
    global fermentation_progress, ethanol_amount, fermentation_running
    if fermentation_running and fermentation_progress < 100:
        # Incrementa o progresso e o etanol produzido
        progress_increment = random.uniform(3, 7)
        fermentation_progress += progress_increment
        if fermentation_progress > 100:
            fermentation_progress = 100
        ethanol_amount += random.uniform(0.2, 0.8)
        
        # Calcula o valor do Brix (reduzindo linearmente do inicial ao final)
        current_brix = initial_brix - (fermentation_progress / 100) * (initial_brix - final_brix)
        if current_brix < final_brix:
            current_brix = final_brix

        label_fermentation_status.config(
            text=f"Progresso: {fermentation_progress:.1f}% | Etanol Produzido: {ethanol_amount:.2f} L | Brix: {current_brix:.1f}"
        )
        
        # Atualiza a "barra" do tanque (preenchimento de baixo para cima)
        fill_height = (fermentation_progress / 100) * (250 - 50)
        new_y = 250 - fill_height
        canvas_fermentation.coords(fermentation_fill, 150, new_y, 350, 250)
        
        # Atualiza a cada 1000 ms (1 segundo, simulando um processo mais lento)
        canvas_fermentation.after(1000, update_fermentation)
    else:
        fermentation_running = False
        label_fermentation_status.config(
            text=f"Fermentação Completa! Progresso: {fermentation_progress:.1f}% | Etanol Produzido: {ethanol_amount:.2f} L | Brix: {final_brix}"
        )
        # Habilita o botão para iniciar a destilação
        button_start_distillation.config(state="normal")

def start_fermentation():
    global fermentation_running, fermentation_progress, ethanol_amount
    fermentation_running = True
    fermentation_progress = 0
    ethanol_amount = 0
    button_start_fermentation.config(state="disabled")
    update_fermentation()

button_start_fermentation = tk.Button(
    frame_fermentation, 
    text="Iniciar Fermentação", 
    font=("Arial", 14), 
    command=start_fermentation, 
    bg="green", 
    fg="white"
)
button_start_fermentation.pack(pady=10)

# Botão para prosseguir para destilação (inicialmente desabilitado)
button_start_distillation = tk.Button(
    frame_fermentation, 
    text="Iniciar Destilação", 
    font=("Arial", 14), 
    command=lambda: show_distillation_frame(), 
    state="disabled", 
    bg="blue", 
    fg="white"
)
button_start_distillation.pack(pady=10)

# ========================
# FRAME DE DESTILAÇÃO
# ========================
frame_distillation = tk.Frame(root, bg="lightgray")
# Este frame será exibido após a fermentação

label_distillation_title = tk.Label(frame_distillation, text="Processo de Destilação", font=("Arial", 16), bg="lightgray")
label_distillation_title.pack(pady=10)

canvas_distillation = tk.Canvas(frame_distillation, width=500, height=300, bg="white")
canvas_distillation.pack(pady=10)

# Desenha um aparelho simples:
# Frasco (para o mosto fermentado)
flask = canvas_distillation.create_oval(50, 100, 150, 200, outline="black", width=2, fill="lightyellow")
# Tubo condensador
condenser = canvas_distillation.create_line(150, 150, 300, 150, fill="black", width=2)
# Recipiente coletor
receiving_container = canvas_distillation.create_rectangle(300, 100, 450, 200, outline="black", width=2)
# Retângulo que representa o etanol coletado (inicia vazio)
distillation_fill = canvas_distillation.create_rectangle(300, 200, 450, 200, fill="orange", outline="")

label_distillation_status = tk.Label(
    frame_distillation, 
    text="Ethanol Destilado: 0 L | Grau do Álcool: 0%", 
    font=("Arial", 14), 
    bg="lightgray"
)
label_distillation_status.pack(pady=5)

def update_distillation():
    global distilled_ethanol, distillation_running, ethanol_amount
    if distillation_running and distilled_ethanol < ethanol_amount:
        distilled_ethanol += random.uniform(0.5, 1.5)
        if distilled_ethanol > ethanol_amount:
            distilled_ethanol = ethanol_amount
        
        # Calcula o grau do álcool: varia de 30% (início) até 96% (quando completa)
        if ethanol_amount > 0:
            alcohol_degree = 30 + (distilled_ethanol / ethanol_amount) * 66
            if alcohol_degree > 96:
                alcohol_degree = 96
        else:
            alcohol_degree = 0
        
        label_distillation_status.config(
            text=f"Ethanol Destilado: {distilled_ethanol:.2f} L | Grau do Álcool: {alcohol_degree:.1f}%"
        )
        
        # Atualiza o preenchimento do recipiente (de y=200 até y=100)
        fill_height = (distilled_ethanol / ethanol_amount) * (200 - 100) if ethanol_amount > 0 else 0
        new_y = 200 - fill_height
        canvas_distillation.coords(distillation_fill, 300, new_y, 450, 200)
        
        # Atualiza a cada 1000 ms (1 segundo, simulando um processo mais lento)
        canvas_distillation.after(1000, update_distillation)
    else:
        distillation_running = False
        label_distillation_status.config(
            text=f"Destilação Completa: {distilled_ethanol:.2f} L destilado | Grau do Álcool: {alcohol_degree:.1f}%"
        )

def start_distillation():
    global distillation_running, distilled_ethanol
    distillation_running = True
    distilled_ethanol = 0
    button_start_distillation_sim.config(state="disabled")
    update_distillation()

button_start_distillation_sim = tk.Button(
    frame_distillation, 
    text="Iniciar Destilação", 
    font=("Arial", 14), 
    command=start_distillation, 
    bg="green", 
    fg="white"
)
button_start_distillation_sim.pack(pady=10)

def show_distillation_frame():
    # Esconde o frame de fermentação e mostra o de destilação
    frame_fermentation.pack_forget()
    frame_distillation.pack(fill="both", expand=True)

# Inicia o loop da interface
root.mainloop()
