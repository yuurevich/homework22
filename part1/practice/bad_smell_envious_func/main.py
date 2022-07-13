# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def calc_cube_volume(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.calc_cube_volume()


if __name__ == "__main__":
    cube = Cube(2, 3, 4)
    cube_volume = CubeVolumeCalculator()
    print(cube_volume.calc_cube_volume(cube))