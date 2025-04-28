class TimeZone:
    def __init__(self, name: str, offset_hours: int, offset_minutes: int):
        self.name = name
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str) and bool(new_name.strip()):
            self._name = new_name.strip()
        else:
            raise ValueError(f'Timezone bad name - {new_name}')

    @property
    def offset_hours(self):
        return self._offset_hours

    @offset_hours.setter
    def offset_hours(self, new_offset_hours: int):
        if isinstance(new_offset_hours, int):
            if -12 <= new_offset_hours <= 14:
                self._offset_hours = new_offset_hours
            else:
                raise ValueError('Offset must be between -12:00 and +14:00.')
        else:
            raise ValueError('Hour offset must be an integer.')

    @property
    def offset_minutes(self):
        return self._offset_minutes

    @offset_minutes.setter
    def offset_minutes(self, new_offset_minutes: int):
        if isinstance(new_offset_minutes, int):
            if abs(new_offset_minutes) <= 59:
                self._offset_minutes = new_offset_minutes
            else:
                raise ValueError('Minutes offset must between -59 and 59.')
        else:
            raise ValueError('Minutes offset must be an integer.')


# tz1 = TimeZone('ABC', -2, -15)
# print(tz1.name)
# print(tz1.offset_hours)
# print(tz1.offset_minutes)
#
# tz1.name = 'XYZ'
# tz1.offset_hours = 12
# tz1.offset_minutes = 0
#
# try:
#     tz1.offset_hours = 67
# except ValueError as e:
#     print(e)
# print(tz1.name, tz1.offset_hours, tz1.offset_minutes)

# пустая строка не должна сохраняться
# for name in ['', None, '    ', 123, (1, 3), True]:
#     try:
#         TimeZone(name, 5, 34)
#     except ValueError as e:
#         print(e)


# try:
#     TimeZone(' Abc ', -20.5, 34)
# except ValueError as e:
#     print(e)
#
# try:
#     TimeZone(' Abc ', -15, 34)
# except ValueError as e:
#     print(e)
#
# try:
#     TimeZone(' Abc ', 15, 34)
# except ValueError as e:
#     print(e)
#
# tz = TimeZone(' Abc ', 10, 34)
# print(tz.name)
# print(tz.offset_hours)
# print(tz.offset_minutes)