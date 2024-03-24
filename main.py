import cv2
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture


class CameraApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = Image()
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # 30 fps
        return self.my_camera

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            # Display image from the texture
            self.my_camera.texture = texture

    def on_stop(self):
        # Release the camera when the app is closed
        self.capture.release()


if __name__ == '__main__':
    CameraApp().run()
