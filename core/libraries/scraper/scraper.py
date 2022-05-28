import requests
import pandas as pd
import lxml
import html5lib

from core.libraries.investpy.resources.resources import get_resources_path

class ScraperApi:

    def get_all_bist_company(self):
        table_bist_sirketler = pd.read_html('https://tr.wikipedia.org/wiki/Borsa_%C4%B0stanbul%27da_i%C5%9Flem_g%C3%B6ren_%C5%9Firketler_listesi')
        a = table_bist_sirketler[3]
        b = table_bist_sirketler[4]
        c = table_bist_sirketler[5]
        c2  = table_bist_sirketler[6]
        d = table_bist_sirketler[7]

        e = table_bist_sirketler[8]
        f = table_bist_sirketler[9]
        g = table_bist_sirketler[10]
        h = table_bist_sirketler[11]
        i = table_bist_sirketler[12]
        i2  = table_bist_sirketler[13]

        j = table_bist_sirketler[14]
        k = table_bist_sirketler[15]
        l = table_bist_sirketler[16]
        m = table_bist_sirketler[17]
        n = table_bist_sirketler[18]
        o = table_bist_sirketler[19]
        o2  = table_bist_sirketler[20]

        p = table_bist_sirketler[21]
        q = table_bist_sirketler[22]
        r = table_bist_sirketler[23]
        s = table_bist_sirketler[24]
        s2  = table_bist_sirketler[25]
        t = table_bist_sirketler[26]
        u = table_bist_sirketler[27]

        u2 = table_bist_sirketler[28]
        v = table_bist_sirketler[29]
        y = table_bist_sirketler[30]
        z = table_bist_sirketler[31]

        tum_bist_sirketleri = pd.concat([a ,b ,c ,c2 ,d, e ,f ,g ,h ,i ,i2, 
        j ,k ,l ,m ,n ,o ,o2, p ,q ,r ,s ,s2 ,t ,u, u2 ,v ,y ,z], axis=0)
        tum_bist_sirketleri = tum_bist_sirketleri.reset_index()
        return tum_bist_sirketleri


    def get_us_sp_500_companies_codes_and_names(self):
        table_sp_500_sirketler = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        df = table_sp_500_sirketler[0][["Symbol", "Security"]].rename(columns={"Symbol": "code", "Security": "title"})
        return df

    def get_germany_dax_40_companies_codes_and_names(self):
        table_dax_40_sirketler = pd.read_html('https://en.wikipedia.org/wiki/DAX')
        return table_dax_40_sirketler[3][["Company", "Ticker symbol"]].rename(columns={"Ticker symbol": "code", "Company": "title"})

    def get_british_ftse_350_companies_codes_names(self):
        table_ftse_350_sirketler = pd.read_html('https://www.fidelity.co.uk/shares/ftse-350/')
        return table_ftse_350_sirketler[0][["EPIC", "Name"]].rename(columns = {"EPIC":"code", "Name": "title"})

    def get_france_cac_40_companies_codes_and_names(self):
        table_cac_40_sirketler1 = pd.read_html('https://www.dividendmax.com/market-index-constituents/cac-40?page=1')
        a = table_cac_40_sirketler1[0][["Company", "Ticker"]].rename(columns={"Company":"title", "Ticker": "code"})
        table_cac_40_sirketler2 = pd.read_html('https://www.dividendmax.com/market-index-constituents/cac-40?page=2')
        b = table_cac_40_sirketler2[0][["Company", "Ticker"]].rename(columns={"Company":"title", "Ticker": "code"})
        return pd.concat([a, b], axis=0).reset_index()


    def get_spain_ibex_35_companies_codes_and_names(self):
        table_cac_40_sirketler1 = pd.read_html('https://www.dividendmax.com/market-index-constituents/ibex-35')
        return table_cac_40_sirketler1[0][["Company", "Ticker"]].rename(columns={"Company":"title", "Ticker": "code"})

    def get_dow_jones_30_companies_codes_and_names(self):
        dow = pd.read_html('https://disfold.com/stock-index/dow-jones/companies/')
        return dow[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})

    def get_russell_2000_companies_codes_and_names(self):
        company_data_list = []
        for i in range(1, 41):
            tbt = pd.read_html(f'https://disfold.com/stock-index/russell-2000/companies/?page={i}')[0][["Company", "Stock Symbol"]]

            for l in range(0, len(tbt)):

                data = {"code": tbt["Stock Symbol"][l], "title" : tbt["Company"][l]}
                company_data_list.append(data)
        
        russel_2000 = pd.DataFrame(company_data_list)
        return russel_2000


    def get_euro_stoxx_50_companies_codes_and_names(self):
        df = pd.read_html("https://en.wikipedia.org/wiki/EURO_STOXX_50")[3][["Ticker", "Name"]].rename(columns={"Name":"title", "Ticker": "code"})
        return df


    def get_hang_seng_companies_codes_and_names(self):
        df1 = pd.read_html(f"https://disfold.com/stock-index/hang-seng/companies/?page=1")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df2 = pd.read_html(f"https://disfold.com/stock-index/hang-seng/companies/?page=2")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df3 = pd.concat([df1, df2], axis=0)
        return df3


    def get_nikkei_225_companies_codes_and_names(self):
        df1 = pd.read_html("https://disfold.com/stock-index/nikkei225/companies/?page=1")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df2 = pd.read_html("https://disfold.com/stock-index/nikkei225/companies/?page=2")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df3 = pd.read_html("https://disfold.com/stock-index/nikkei225/companies/?page=3")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df4 = pd.read_html("https://disfold.com/stock-index/nikkei225/companies/?page=4")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df5 = pd.read_html("https://disfold.com/stock-index/nikkei225/companies/?page=5")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})

        df = pd.concat([df1, df2, df3, df4, df5], axis=0)
        return df 


    def get_sse_1740_companies_codes_and_names(self):
        company_data_list = []
        for i in range(1, 36):
            tbt = pd.read_html(f'https://disfold.com/stock-index/sse-composite/companies/?page={i}')[0][["Company", "Stock Symbol"]]

            for l in range(0, len(tbt)):

                data = {"code": tbt["Stock Symbol"][l], "title" : tbt["Company"][l]}
                company_data_list.append(data)

        sse_chine_1740 = pd.DataFrame(company_data_list)
        return sse_chine_1740
    
    def get_ftse_mib_40_companies_codes_and_names(self):
        df = pd.read_html("https://disfold.com/stock-index/ftse-mib/companies/")[0][["Company", "Stock Symbol"]]
        return df
        

    def get_s_p_tsx_230_companies_codes_and_names(self):
        df1 = pd.read_html("https://disfold.com/stock-index/tsx-composite/companies/?page=1")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df2 = pd.read_html("https://disfold.com/stock-index/tsx-composite/companies/?page=2")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df3 = pd.read_html("https://disfold.com/stock-index/tsx-composite/companies/?page=3")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df4 = pd.read_html("https://disfold.com/stock-index/tsx-composite/companies/?page=4")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})
        df5 = pd.read_html("https://disfold.com/stock-index/tsx-composite/companies/?page=5")[0][["Company", "Stock Symbol"]].rename(columns={"Company":"title", "Stock Symbol": "code"})

        df = pd.concat([df1, df2, df3, df4, df5], axis=0)
        return df 


    def get_nasdaq_3000_companies_codes_and_names(self):
        company_data_list = []
        for i in range(1, 61):
            tbt = pd.read_html(f'https://disfold.com/stock-index/nasdaq-composite/companies/?page={i}')[0][["Company", "Stock Symbol"]]

            for l in range(0, len(tbt)):

                data = {"code": tbt["Stock Symbol"][l], "title" : tbt["Company"][l]}
                company_data_list.append(data)

        nasdaq_3000 = pd.DataFrame(company_data_list)
        return nasdaq_3000      

    def get_universal_investpy_company_list(self):
        company = get_resources_path() + "\\" + "stocks.csv"
        df = pd.read_csv(company)
        df_company = df[(df["country"]=="turkey") | (df["country"]=="hong kong") | (df["country"]=="united states") | (df["country"]=="france") | (df["country"]=="spain") | (df["country"]=="united kingdom") | (df["country"]=="canada") | (df["country"]=="germany") | (df["country"]=="italy") | (df["country"]=="japan") | (df["country"]=="china") | (df["country"]=="india")]
        return df_company