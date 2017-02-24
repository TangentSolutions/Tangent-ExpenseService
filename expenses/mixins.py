class MultiSerializerMixin:

    serializer_map = {}
    default_serializer = None

    def get_serializer_class(self):
        """
        ..
        """

        client_serializer_map = {
            "create": ClientAppointmentSerializer,
            "list": ReadOnlyClientAppointmentSerializer,
            "retrieve": ReadOnlyClientAppointmentSerializer,
            "default": ClientAppointmentSerializer
        }

        practitioner_serializer_map = {
            "create": AppointmentSerializer,
            "list": ReadOnlyPractitionerAppointmentSerializer,
            "list": AppointmentListViewSerializer,
            "retrieve": ReadOnlyPractitionerAppointmentSerializer,
            "default": AppointmentSerializer,
        }


        # is_practitioner will fail on anon user
        # anon users _can only create appointment_
        if self.request.user.is_anonymous():
            return ClientAppointmentSerializer

        if self.request.user.is_practitioner:
            default_serializer = practitioner_serializer_map.get("default")
            return practitioner_serializer_map.get(self.action, default_serializer)
        else:
            default_serializer = client_serializer_map.get("default")
            return client_serializer_map.get(self.action, default_serializer)
