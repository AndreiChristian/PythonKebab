import dearpygui.dearpygui as dpg


def increment():

    # print("I increment!")

    value = int(dpg.get_value("number text"))

    dpg.set_value("number text", value + 1)


def decrement():

    # print("I decrement!")

    value = int(dpg.get_value("number text"))

    if value > 0:

        dpg.set_value("number text", value - 1)


dpg.create_context()

dpg.create_viewport(title='PythonKebab', width=600, height=800)


with dpg.window(label="Example Window", tag="Primary Window"):

    dpg.add_button(label="INCREMENT +", callback=increment)

    dpg.add_text(0, tag="number text")

    dpg.add_button(label="DECREMENT -", callback=decrement)


dpg.setup_dearpygui()

dpg.show_viewport()

dpg.set_primary_window("Primary Window", True)

dpg.start_dearpygui()

dpg.destroy_context()
