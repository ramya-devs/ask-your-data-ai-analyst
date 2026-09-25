import os,re,sqlite3
import pandas as pd,streamlit as st,plotly.express as px
from google import genai
st.set_page_config(page_title='AskYourData',layout='wide')
st.title('AskYourData - AI Analyst')
def sql_for(q,schema):
 c=genai.Client(api_key=os.environ['GEMINI_API_KEY'])
 prompt=f'''Convert the question to ONE read-only SQLite SELECT query.
Table sales({schema}). Return SQL only. Understand English or Tanglish.
Question: {q}'''
 s=c.models.generate_content(model='gemini-3.8-flash',contents=prompt).text.strip().strip('`')
 if not re.match(r'^(SELECT|WITH)\b',s,re.I) or re.search(r'\b(INSERT|UPDATE|DELETE|DROP|ALTER|ATTACH|PRAGMA)\b',s,re.I): raise ValueError('Unsafe SQL blocked')
 return s
con=sqlite3.connect('sales.db',check_same_thread=False)
schema=', '.join(r[1] for r in con.execute('PRAGMA table_info(sales)'))
q=st.text_input('Ask your data',placeholder='Velachery la Saree sales enna?')
if st.button('Ask') and q:
 try:
  sql=sql_for(q,schema); out=pd.read_sql_query(sql,con)
  st.subheader('Generated SQL'); st.code(sql,'sql')
  st.subheader('Result'); st.dataframe(out,use_container_width=True)
  nums=out.select_dtypes('number').columns
  if len(out.columns)>=2 and len(nums): st.plotly_chart(px.bar(out,x=out.columns[0],y=nums[0]),use_container_width=True)
 except Exception as e: st.error(str(e))
