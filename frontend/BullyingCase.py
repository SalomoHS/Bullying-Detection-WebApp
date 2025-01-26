import streamlit as st
import plotly.graph_objects as go

st.title("Talking About Data")


years = [2020, 2021, 2022]
cases = [119, 53, 226]

# Create a bar chart
fig_bar_1 = go.Figure(go.Bar(x=years, y=cases, marker=dict(
                color="#FFC145",
                line=dict(color='rgb(248, 248, 249)', width=1)
            )))

# Update layout for the chart
fig_bar_1.update_layout(
    title="Bullying Cases per Year",
    xaxis_title="Year",
    yaxis_title="Number of Cases",
    xaxis=dict(
        tickvals=[2020, 2021, 2022],  # Show only these years
        ticktext=["2020", "2021", "2022"]  # Set labels for the ticks
    ),
    template="plotly_dark"
)

bullying_types = ['Physical Bullying', 'Verbal Bullying', 'Psychological Bullying']
percentages = [55.5, 29.3, 15.2]

# Create a pie chart
fig_pie_1 = go.Figure(go.Pie(labels=bullying_types,textfont=dict(color='black'),values=percentages, hole=0.3, marker=dict(colors=['#FB4141', '#FFEB00', '#5CB338'], line=dict(color='rgb(248, 248, 249)', width=1))))
# Update layout for the chart
fig_pie_1.update_layout(
    title="Types of Bullying that Victims Often Experience",
    template="plotly_dark"
)

top_labels = ['Elementary School','Junior High Scool','Senior High School']
x_data = [[26,25,19]]  
y_data = ['sdfsfssdfsdfdsdf']
colors = ['#FA4032', '#FA812F',
          '#FAB12F', 'rgba(164, 163, 204, 0.85)',
          'rgba(190, 192, 213, 1)']
fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

# fig.update_traces(width=0.2)

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    # paper_bgcolor='rgb(248, 248, 255)',
    # plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=0, r=100, t=80, b=60),
    showlegend=False,template="plotly_dark",
    title=dict(
                            text = "Education Level of Bullying Victims",
                            x = 0.5,
                            y = 0.90,
                            xanchor =  'center',
                            yanchor = 'top',
                            #pad = dict(
                            #            t = 0
                            #           ),
                            )
    # height=250
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text= str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='black'),
                            showarrow=False,valign='middle'))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(255, 255, 255)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text = str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='black'),
                                    showarrow=False,valign='middle'))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(255, 255, 255)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations,template="plotly_dark", height=250)
# fig.update_traces(width=0.2)

# Display the chart in Streamlit

st.header("2022")
st.markdown("""Data obtained based on survey from Indonesian Child Protection Commission (KPAI) and Federation of Indonesian Teachers Union (FSGI) with recorded **226 cases** of bullying occurred in **2022**. <a href="https://www.dpr.go.id/berita/detail/id/46802/t/Pemerintah%20Harus%20Petakan%20Faktor%20Penyebab%20Bullying%20Anak">Read more</a>""",unsafe_allow_html=True)
col1, col2 = st.columns(2,gap='large')

with col1:
    st.plotly_chart(fig_bar_1)

with col2:
    st.plotly_chart(fig_pie_1)

st.plotly_chart(fig)





st.header("2018")
top_labels = ['No','Yes']
x_data = [[100-18, 18],
          [100-22, 22],
          [100-14, 14],
          [100-22, 22],
          [100-19, 19],
          [100-20, 20]]
y_data = ['I was hit<br>and ordered around<br>by other students',
          'Other students<br>take or destroy my stuff',
          'I was threatened<br>by another student',
          'I was mocked<br>by another student',
          'Other students<br>deliberately excluded me',
          'Other students<br>spread harmful rumors<br>about me']

colors = ['#ABBA7C', '#F09319',
          'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
          'rgba(190, 192, 213, 1)']
fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    margin=dict(l=120, r=10, t=120, b=10),
    showlegend=False,
    title=dict(
                            text = "Bullied at least a few times a month",
                            x = 0.5,
                            y = 0.90,
                            xanchor =  'center',
                            yanchor = 'top',
                            #pad = dict(
                            #            t = 0
                            #           ),
                            )
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='black'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='black'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(248, 248, 255)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations,template="plotly_dark")
# fig.update_traces(width=1)

st.markdown("""Based on the results of the National Survey on the Life Experiences of Children and Adolescents (SNPHAR) by the Indonesian Ministry of Women's Empowerment and Child Protection (KPPPAI) in 2018, there are several actions that often occur in cases of bullying. 
            <a href="https://www.scribd.com/document/559700353/Fakta-kunci-perundungan-di-Indonesia">Read more</a>""",unsafe_allow_html=True)


st.plotly_chart(fig)

st.title("News Coverage")

news = [
    {
        "title": "Chronology of elementary school student who blinded his friend in Gresik",
        "summary": "A second-grade student with the initials SAH in Menganti, Gresik, was left permanently blind after her eyes were poked out with meatball skewers by her seniors. The victim also claimed to have been bullied since grade 1, causing trauma. ...",
        "link": "https://tirto.id/kronologi-siswa-colok-mata-temannya-hingga-buta-di-sd-gresik-gQbj",
    },
    {
        "title": "2 Bully Students in Cilacap Junior High School Become Suspects",
        "summary": "Cilacap Police named two students of SMP Negeri 2 Cimanggu, MK (15) and WS (14), as suspects in a bullying case against FF (14). Head of Central Java Police Public Relations Kombesus Satake Bayu said the determination was made by investigators after examining a number of witnesses and video footage circulating on social media. ...",
        "link": "https://www.cnnindonesia.com/nasional/20230929105441-12-1005051/2-siswa-pelaku-bully-di-smp-cilacap-jadi-tersangka",
    },
    {
        "title": "High school student bullied into psychiatric hospital, KPAI highlights school protection",
        "summary": "The Indonesian Child Protection Commission (KPAI) highlighted a series of bullying cases that occurred in the educational environment. KPAI said that the series of bullying incidents that have occurred recently must be taken seriously. ...",
        "link": "https://news.detik.com/berita/d-7523197/siswa-sma-di-bully-hingga-masuk-rsj-kpai-soroti-perlindungan-sekolah",
    },
]
for item in news:
    # Create a card for each news item
    with st.container():
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; padding: 15px; border-radius: 10px; margin-bottom: 15px; cursor: pointer;">
                <h3>{item['title']}</h3>
                <p>{item['summary']}</p>
                <a href="{item['link']}" target="_blank" style="text-decoration: none; color: #1e90ff;">Read more</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
