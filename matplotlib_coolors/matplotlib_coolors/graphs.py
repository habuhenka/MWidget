def mG(void = 0):
  if void == 90811:
    print(
"""fig, axes = plt.subplots(3, 7, figsize=(30, 20))
for row in range(3):
  for col in range(7):
    sns.stripplot(
      ax=axes[row, col], data=voice[features],
      y=features[(row * 7) + col], x=voice.label)"""
        )
  
def hmG(void = 0):
  if void == 90811:
    print(
"""plt.subplots(figsize =(12,12))
sns.heatmap(df_num.corr(), cmap = rp.palette_cmap, square=True, cbar_kws=dict(shrink =.82),fmt='.2f', 
            annot=True, vmin=-1, vmax=1, linewidths=2,linecolor='black',annot_kws=dict(fontsize =18))
plt.title("\\nPearson Correlation Of Features\\n", fontsize=25)
plt.xticks(rotation=90)
plt.show()"""
  )
  
def brH(void = 0):
  if void == 90811:
    print(
"""plt.subplots(figsize=(20,10))
p = sns.countplot(y=df.job_title,order=job_count,palette=palette, saturation=1, edgecolor='#1c1c1c',linewidth=4)
p.axes.set_title('\\nData Science Job\\n', fontsize=25)
p.axes.set_xlabel('Total',fontsize= 20)
p.axes.set_ylabel('Job_title',fontsize=20)
for container in p.containers:
  p.bar_label(container,label_type='edge',padding=-10,size=25,color='black',rotation=0,
              bbox={'boxstyle':'round','pad':0.4,'facecolor':'orange','edgecolor':'#1c1c1c','linewidth':4,'alpha':1})

sns.despine(left=True, bottom=True)
plt.show()"""
  )

def pC(void = 0):
  if void == 90811:
    print(
"""plt.subplots(figsize=(12,12))
label = "Middle", 'Large', 'Small'
size = 0.5

wedges,texts,autotexts = plt.pie([company_size_count[0],company_size_count[1],company_size_count[2]],
                                 explode=(0,0,0),
                                 autopct='%.2f%%',
                                 pctdistance=0.72,
                                 textprops=dict(size=20, color='White'),
                                 radius=.9,
                                 shadow=True,
                                 colors=["#11264e","#008b99","#ef3f28"],
                                 wedgeprops=dict(width=size,edgecolor='black',linewidth=3),
                                 startangle=100)
plt.legend(wedges,label,title = 'Ukuran Perusahaan',loc='center left',bbox_to_anchor=(1,0,0.5,1),edgecolor='black')
plt.title('Ukuran Perusahaan :',size=25)
plt.show()"""
  )