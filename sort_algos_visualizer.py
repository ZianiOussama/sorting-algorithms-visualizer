from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from random import randint
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.textinput import TextInput
import threading
import time
from kivy.core.window import Window
from kivy.uix.widget import Widget


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.array_len = 100
        self.speed = 500
        self.new_array()

    def new_array(self):
        self.array = [randint(5, Window.height - 100) for _ in range(self.array_len)]
        self.draw()  # draws the array
        
    def draw(self, *args):
        width = Window.width
        self.canvas.clear()

        with self.canvas:
            pos = 0
            for i in range(len(self.array)):
                Rectangle(pos=(pos, 100), size=(width / len(self.array) - 2, self.array[i]))
                pos += width / len(self.array)

    def clock(self):
        Clock.schedule_interval(self.draw, 0)

    def start_threading(self, func):
        t1 = threading.Thread(target=func)
        t2 = threading.Thread(target=self.clock)

        t1.start()
        t2.start()

    def bubble_sort(self):
        for j in range(len(self.array)):
            for i in range(len(self.array) - (1 + j)):
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                time.sleep(1 / self.speed)

    def set_merge_sort(self, *args):
        a = [i for i in range(self.array_len)]
        self.merge_sort(a)

    def merge_sort(self, array, *args):
        if len(array) < 2:
            return array

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        self.merge_sort(left)
        self.merge_sort(right)
        array_copy = self.array[:]

        i = j = k = 0
        while i < len(left) and j < len(right):
            time.sleep(1 / self.speed)
            if array_copy[left[i]] < array_copy[right[j]]:
                self.array[array[k]] = array_copy[left[i]]
                i += 1
                k += 1
            elif array_copy[left[i]] > array_copy[right[j]]:
                self.array[array[k]] = array_copy[right[j]]
                j += 1
                k += 1
            else:
                self.array[array[k]] = array_copy[left[i]]
                i += 1
                k += 1
                self.array[array[k]] = array_copy[right[j]]
                k += 1
                j += 1

        while i < len(left):
            self.array[array[k]] = array_copy[left[i]]
            i += 1
            k += 1
        while j < len(right):
            self.array[array[k]] = array_copy[right[j]]
            j += 1
            k += 1

    def set_quick_sort(self, *args):
        a = [i for i in range(self.array_len)]
        self.quick_sort(a)

    def quick_sort(self, array, *args):
        if len(array) < 2:
            return array

        piv = len(array) - 1
        i = 0
        while len(array) > i != piv >= 0:
            if self.array[array[i]] > self.array[array[piv]]:
                self.array.insert(array[-1] + 1, self.array[array[i]])
                self.array.remove(self.array[array[i]])
                piv -= 1
                i -= 1
            i += 1
            time.sleep(1/self.speed)

        l, r = array[:piv], array[piv:]
        self.quick_sort(l)
        self.quick_sort(r)
        array[:piv], array[piv:] = l, r

    def radix_sort(self):
        max_len = 1
        for i in self.array:
            if len(str(i)) > max_len:
                max_len = len(str(i))

        digit = -1
        for _ in range(max_len):
            buckets = [[] for _ in range(10)]
            for num in self.array:
                num_str = str(num)
                try:
                    char = num_str[digit]
                    buckets[int(char)].append(int(num_str))
                except IndexError:
                    buckets[0].append(int(num_str))

            idx = 0
            for bucket in buckets:
                for i in bucket:
                    self.array[idx] = i
                    idx += 1
                    time.sleep(1 / self.speed)

            digit -= 1


widget = MyWidget()


class Input(TextInput):
    def on_text(self, *args):
        try:
            int(self.text)
        except ValueError:
            pass
        else:
            if int(self.text) <= 10_000:
                widget.array_len = int(self.text)
                widget.new_array()


class NewArrayButton(Button):
    def __init__(self):
        super().__init__()
        self.text = '+ NEW ARRAY'

    def on_release(self):
        widget.new_array()


class BubbleSortButton(Button):
    def __init__(self):
        super().__init__()
        self.text = 'START (bubble sort)'

    def on_release(self):
        widget.start_threading(widget.bubble_sort)


class MergeSortButton(Button):
    def __init__(self):
        super().__init__()
        self.text = 'START (merge sort)'

    def on_release(self):
        widget.start_threading(widget.set_merge_sort)


class QuickSortButton (Button):
    def __init__(self):
        super().__init__()
        self.text = 'START (quick sort)'

    def on_release(self):
        widget.start_threading(widget.set_quick_sort)


class RadixSortButton (Button):
    def __init__(self):
        super().__init__()
        self.text = 'START (radix sort)'

    def on_release(self):
        widget.start_threading(widget.radix_sort)


class ButtonsGrid(GridLayout):
    def __init__(self):
        super().__init__()
        self.cols = 3
        self.size_hint_y = None
        self.size = [Window.width, 100]
        self.add_widget(NewArrayButton())
        self.add_widget(BubbleSortButton())
        self.add_widget(MergeSortButton())
        self.add_widget(Input())
        self.add_widget(QuickSortButton())
        self.add_widget(RadixSortButton())


class MyGrid(GridLayout):
    def __init__(self):
        super().__init__()
        self.rows = 2
        self.add_widget(widget)
        self.add_widget(ButtonsGrid())


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    app = MyApp()
    app.run()
