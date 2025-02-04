from collections import defaultdict

def city_data(n):
    
    data_dict = defaultdict(int) # defaultdictかなんちゃらをここで作って、理想的な辞書をつくる
    totalnum_people = 0
    total_comsumption = 0
    
    while n > 0:
        
        num_people, consumption = int(input().split())
        
        consumption_per_people = consumption // num_people
        totalnum_people += num_people
        total_comsumption += consumption
        
        data_dict[consumption_per_people] += num_people
        
        n += -1
        
    return total_comsumption/totalnum_people, data_dict # consumo medio and data to print
    
    
    
def main():
    num_properties = int(input())
    avg_consumption_per_people, data_dict = city_data(num_properties)
    


if __name__ == "(__main__)":
    main()