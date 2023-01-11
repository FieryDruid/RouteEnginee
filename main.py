from tkinter import Tk, Widget, StringVar
from tkinter.ttk import Frame, Label, Button, Combobox, Entry
from typing import NamedTuple, Optional, Callable


class Position(NamedTuple):
    column: int
    row: int


class MainWindow:

    def __init__(self, title: str = 'Routes'):
        self._window = Tk()
        self._window.title(title)

        self._create_frame()

        self._create_engineer_widgets()
        self._create_client_widgets()
        self._create_material_widgets()
        self._create_point_a_widgets()

        exit_button = self._create(Button, self._main_frame, 'exit', self._close_window)
        self._set_grid(exit_button, Position(0, 4))

    def _create_engineer_widgets(self):
        engineers = [1, 2, 3, 4, 5]
        self.engineer = StringVar(value=str(engineers[0]))
        engineer_label = self._create(Label, self._main_frame, 'Engineer:')
        self._set_grid(engineer_label, Position(0, 0))
        self.engineer_combobox = self._create(
            Combobox, self._main_frame, textvariable=self.engineer, values=engineers, state='readonly'
        )

        self._set_grid(self.engineer_combobox, Position(1, 0))

    def _create_client_widgets(self):
        clients = [1, 2, 3, 4, 5]
        self.client = StringVar()
        client_label = self._create(Label, self._main_frame, 'Client:')
        self._set_grid(client_label, Position(0, 2))
        self.client_combobox = self._create(
            Combobox, self._main_frame, textvariable=self.client, values=clients
        )

        self._set_grid(self.client_combobox, Position(1, 2))

    def _create_material_widgets(self):
        self.material = StringVar()
        client_label = self._create(Label, self._main_frame, 'Material:')
        self._set_grid(client_label, Position(0, 3))
        self.material_entry = self._create(
            Entry, self._main_frame, textvariable=self.material
        )

        self._set_grid(self.material_entry, Position(1, 3))

    def _create_point_a_widgets(self):
        points = [1, 44, 23, 64]
        self.point_a = StringVar()
        client_label = self._create(Label, self._main_frame, 'From:')
        self._set_grid(client_label, Position(0, 5))
        self.point_a_combobox = self._create(
            Combobox, self._main_frame, textvariable=self.point_a, values=points
        )

        self._set_grid(self.material_entry, Position(1, 5))

    def run(self) -> None:
        self._window.mainloop()

    @staticmethod
    def _create(
            element: type[Widget],
            master: Tk | Widget,
            text: str | None = None,
            command: Optional[Callable] = None,
            **initial_kwargs
    ) -> Widget:
        initial_params = {}
        if text:
            initial_params['text'] = text
        if command:
            initial_params['command'] = command

        return element(master=master, **initial_params, **initial_kwargs)

    @staticmethod
    def _set_grid(element: Widget, position: Position | None = None):
        grid_params = {}
        if position:
            grid_params['column'] = position.column
            grid_params['row'] = position.row
        element.grid(**grid_params)

    def _create_frame(self):
        self._main_frame = self._create(Frame, self._window, padding=10)
        self._set_grid(self._main_frame)

    def _close_window(self):
        print(self.engineer.get())
        print(self.client.get())
        print(self.material.get())
        print(self.point_a.get())
        self._window.destroy()


if __name__ == '__main__':
    window = MainWindow()
    window.run()
