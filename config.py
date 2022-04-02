base_url = 'https://tass.ru/userApi/getNewsFeed'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.47',
    'cookie': 'SLG_G_WPT_TO=ru; __js_p_=503,1800,0,0; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; __jhash_=816; __jua_=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F99.0.4844.84%20Safari%2F537.36%20OPR%2F85.0.4341.47; __hash_=3efb822c3d5c0200c57a4ee13804055e; __lhash_=02c65abce273291181765a9f84ff06df; tass_uuid=4DC10674-EAE7-48B5-A596-47C6C8FC9B2C',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/json',
}
# params = {'limit' : 50}


fields = ['id', 'title','image','link']