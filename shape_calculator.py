import geometry_utils

dicts = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area
}


print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter")

mod = input("Enter the operation you want to perform: ")

if mod == "circle_area":
    radius = float(input("Enter radius: "))
    if radius <= 0:
        print("Input Error: Dimensions must be positive")
    else:
        result = dicts[mod](radius)
        print("Result:", result)

elif mod == "circle_perimeter":
    radius = float(input("Enter radius: "))
    if radius <= 0:
        print("Input Error: Dimensions must be positive")
    else:
        result = dicts[mod](radius)
        print("Result:", result)

elif mod == "rectangle_area":
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    if width <= 0 or height <= 0:
        print("Input Error: Dimensions must be positive")
    else:
        result = dicts[mod](width, height)
        print("Result:", result)

elif mod == "rectangle_perimeter":
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    if width <= 0 or height <= 0:
        print("Input Error: Dimensions must be positive")
    else:
        result = dicts[mod](width, height)
        print("Result:", result)

elif mod == "triangle_area":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    if base <= 0 or height <= 0:
        print("Input Error: Dimensions must be positive")
    else:
        result = dicts[mod](base, height)
        print("Result:", result)

else:
    print("Invalid operation")