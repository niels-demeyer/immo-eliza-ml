from ImmoClass_file import ImmoClass

immo = ImmoClass("HOUSE")
immo.print_non_numerical_column_values()  # Assuming this method exists and modifies self.df
print(immo.column_values)
