import os
import random
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Imagens Aleatórias")
        
        self.image_folder = ""
        self.images = []
        self.current_image_index = 0
        self.shown_images = set()

        self.label = Label(root)
        self.label.pack()

        self.next_button = Button(root, text="Próxima Imagem", command=self.show_next_image)
        self.next_button.pack()

        self.load_button = Button(root, text="Carregar Pasta", command=self.load_folder)
        self.load_button.pack()

    def load_folder(self):
        self.image_folder = filedialog.askdirectory()
        if self.image_folder:
            self.images = [os.path.join(self.image_folder, f) for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            random.shuffle(self.images)
            self.current_image_index = 0
            self.shown_images = set()
            self.show_next_image()

    def show_next_image(self):
        if self.current_image_index < len(self.images):
            image_path = self.images[self.current_image_index]
            self.shown_images.add(image_path)
            self.current_image_index += 1

            image = Image.open(image_path)
            image.thumbnail((800, 600))  # Redimensiona a imagem para caber na janela
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo  # Mantém uma referência para evitar garbage collection
        else:
            self.label.config(text="Todas as imagens foram mostradas!")
            self.next_button.config(state="disabled")

if __name__ == "__main__":
    root = Tk()
    app = ImageViewer(root)
    root.mainloop()