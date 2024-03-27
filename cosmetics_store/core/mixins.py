class FormControlFieldsMixin:
    fields_requiring_form_control = ()

    def _make_fields_form_control(self):
        field_names = self.fields.keys() if "__all__" else self.fields_requiring_form_control
        for field_name in field_names:
            self.fields[field_name].widget.attrs["class"] = "form-control"