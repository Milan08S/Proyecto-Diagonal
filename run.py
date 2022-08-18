from streamlit import bootstrap

real_script = 'Proyecto prueba/streamlit_example_app/view/MainView.py'

bootstrap.run(real_script, f'run.py {real_script}', [], {})
