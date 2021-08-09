
class BootstrapForm:
    """
    A mixin which gives fields of the forms HTML classes for styling.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_default_style()

    def __add_default_style(self):
        for value, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' main-button custom-field'
