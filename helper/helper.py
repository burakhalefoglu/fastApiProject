
class Helper:

    def date_obj_to_str(self, element: int) -> str:
        if element <= 9:
            return "0" + str(element)
        return str(element)
