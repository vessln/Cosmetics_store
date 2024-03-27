class FormControlFieldsMixin:
    fields_requiring_form_control = ()

    def _make_fields_form_control(self):
        for field_name in self.form_control_field_names:
            self.fields[field_name].widget.attrs["class"] = "form-control"

    @property
    def form_control_field_names(self):
        if self.fields_requiring_form_control == "__all__":
            return self.fields.keys()

        return self.fields_requiring_form_control
