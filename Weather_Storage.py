from typing import List, Optional



class WeatherRecord:
    def __init__(self, date: str, city: str, temperature: float):
        self.date = date          
        self.city = city
        self.temperature = temperature

    def __str__(self):
        return f"[{self.date}] {self.city}: {self.temperature}°C"



class WeatherDataStorage:
    def __init__(self, years: List[int], cities: List[str]):
        self.years = years
        self.cities = cities
        self.year_index = {year: i for i, year in enumerate(years)}
        self.city_index = {city: j for j, city in enumerate(cities)}

       
        self.data = [[None for _ in cities] for _ in years]

   
    def insert(self, record: WeatherRecord):
        year = int(record.date.split("/")[-1])
        if year in self.year_index and record.city in self.city_index:
            i, j = self.year_index[year], self.city_index[record.city]
            self.data[i][j] = record
            print("✅ Record inserted.")
        else:
            print("❌ Invalid year or city.")

    
    def delete(self, date: str, city: str):
        year = int(date.split("/")[-1])
        if year in self.year_index and city in self.city_index:
            i, j = self.year_index[year], self.city_index[city]
            self.data[i][j] = None
            print("🗑 Record deleted.")
        else:
            print("❌ Invalid year or city.")

   
    def retrieve(self, city: str, year: int) -> Optional[WeatherRecord]:
        if year in self.year_index and city in self.city_index:
            i, j = self.year_index[year], self.city_index[city]
            record = self.data[i][j]
            if record:
                print(f"🌡 {record}")
                return record
            else:
                print("⚠ No record found.")
                return None
        else:
            print("❌ Invalid year or city.")
            return None

   
    def row_major_access(self):
        print("\n🔍 Row-Major Traversal:")
        for i, year in enumerate(self.years):
            for j, city in enumerate(self.cities):
                print(f"({year}, {city}) = {self.data[i][j]}")
        print("✅ Row-major traversal complete.")

   
    def column_major_access(self):
        print("\n🔍 Column-Major Traversal:")
        for j, city in enumerate(self.cities):
            for i, year in enumerate(self.years):
                print(f"({year}, {city}) = {self.data[i][j]}")
        print("✅ Column-major traversal complete.")

   
    def handle_sparse_data(self):
        print("\n📦 Sparse Representation:")
        sparse_repr = {}
        for i, year in enumerate(self.years):
            for j, city in enumerate(self.cities):
                if self.data[i][j] is not None:
                    sparse_repr[(year, city)] = self.data[i][j].temperature
        for key, val in sparse_repr.items():
            print(f"{key}: {val}°C")
        return sparse_repr

    
    def analyze_complexity(self):
        print("\n📊 Time & Space Complexity:")
        print("Insert/Delete/Retrieve: O(1) time, O(1) space")
        print(f"Row/Column Traversal: O({len(self.years) * len(self.cities)}) time")
        print("Sparse Representation: O(N) space, where N = number of non-missing records")



if __name__ == "__main__":
    print("📅 Enter number of years:")
    num_years = int(input())
    print("📅 Enter years:")
    years = [int(input(f"Year {i+1}: ")) for i in range(num_years)]

    print("🏙 Enter number of cities:")
    num_cities = int(input())
    print("🏙 Enter cities:")
    cities = [input(f"City {i+1}: ") for i in range(num_cities)]

    storage = WeatherDataStorage(years, cities)

    while True:
        print("\n📋 --- Weather Data Menu ---")
        print("1. Insert Record")
        print("2. Delete Record")
        print("3. Retrieve Record")
        print("4. Row-Major Traversal")
        print("5. Column-Major Traversal")
        print("6. Sparse Representation")
        print("7. Complexity Analysis")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Date (DD/MM/YYYY): ")
            city = input("City: ")
            temp = float(input("Temperature: "))
            record = WeatherRecord(date, city, temp)
            storage.insert(record)

        elif choice == "2":
            date = input("Date (DD/MM/YYYY): ")
            city = input("City: ")
            storage.delete(date, city)

        elif choice == "3":
            year = int(input("Year: "))
            city = input("City: ")
            storage.retrieve(city, year)

        elif choice == "4":
            storage.row_major_access()

        elif choice == "5":
            storage.column_major_access()

        elif choice == "6":
            storage.handle_sparse_data()

        elif choice == "7":
            storage.analyze_complexity()

        elif choice == "0":
            print("👋 Exiting program.")
            break

        else:
            print("❌ Invalid choice. Try again.")
