
class EditorKey:
    def __init__(self):
        self.colorDict = {}
        # self.key_type = key_type
        # self.rgba_string = rgba_string
        # self.hex_string = self.RGBa2Hex(self.rgba_string)
        # self.colorDict = {
        #     self.key_type: {
        #         "Color": {
        #             "RGBa": self.rgba_string,
        #             "HEX": self.hex_string
        #         }}}

    def RGBa2Hex(self, RGBa_str) -> str:
        def string2array(string: str) -> list[float]:
            colorArray = string.split(" ")
            arrayFloat = [float(x) for x in colorArray]
            if len(arrayFloat) == 3:
                arrayFloat.append(1)
            return arrayFloat

        def rgba2hex(rgba) -> str:
            r = int(rgba[0] * 255)
            g = int(rgba[1] * 255)
            b = int(rgba[2] * 255)
            a = f"{int(rgba[3]*100)}"
            string = f'{r:02x}{g:02x}{b:02x}'.upper()
            if rgba[3] != 1:
                string += f" {a:0>2}"
            return string

        array = string2array(RGBa_str)
        return rgba2hex(array)

    def addKeyDict(self, keyType: str, rgba: str) -> None:
        hex_str = self.RGBa2Hex(rgba)
        self.colorDict[keyType] = {"RGBa": rgba, "Hex": hex_str}


colorList = []
editorKey = EditorKey()

with open("xcode.txt", "r") as openfile:
    text_array = openfile.readlines()
    text_array = [line.strip().rstrip() for line in text_array]

for index, line in enumerate(text_array):
    line = line.replace("<key>", "").replace("</key>", "")
    line = line.replace("<string>", "").replace("</string>", "")
    text_array[index] = line

for index, line in enumerate(text_array):
    if index % 2 == 1:
        continue
    key_name = text_array[index]
    rgba_str = text_array[index+1]
    editorKey.addKeyDict(key_name, rgba_str)

for item in editorKey.colorDict:
    item_title = f"{item}  "
    item_color = editorKey.colorDict[item]["Hex"]
    item_string = f"{item_title:-<30}  {item_color}\n"
    colorList.append(item_string)

with open("xcode-format.txt", "w") as writefile:
    writefile.writelines(colorList)
