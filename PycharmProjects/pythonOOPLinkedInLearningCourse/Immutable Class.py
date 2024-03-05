from dataclasses import dataclass

# frozen = True means that class in immutable
@dataclass(frozen = True)
class ImmutableClass():
    value1: str = "Value 1"
    value2: int = 0

    def changeFunc(self, newval):
        self.value2 = newval

obj = ImmutableClass("IninValue", 20)
obj.changeFunc(40)
#obj.value1 = "Change Value"
print(obj.value1, obj.value2)
