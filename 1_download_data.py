import os
i2m = list(zip(range(1,13), ['Gener','Febrer','Marc','Abril','Maig','Juny','Juliol','Agost','Setembre','Octubre','Novembre','Desembre']))
for year in range(2024, 2019, -1):
    for month, month_name in i2m:     
        if (month > 5) and (year>2023): continue 
        os.system(f'curl -L -o "{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z" "https://opendata-ajuntament.barcelona.cat/resources/bcn/BicingBCN/{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z"')
