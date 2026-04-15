import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# MODERN UI CSS
# -------------------------------
st.markdown("""
<style>

/* Main background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #111827;
    color: white;
}

/* Card style */
.card {
    background: #1f2937;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    margin-bottom: 25px;
    text-align: center;
}

/* Titles */
h1, h2, h3 {
    color: #f9fafb;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: #1f2937;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.3);
}

/* Padding fix */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown("<h1 style='text-align:center;'>📊 College Placement Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# LOAD DATA (FIXED PATH ⚠️)
# -------------------------------
df = pd.read_csv("E:\Campus placement analysis\data\Placement_Data_Full_Class.csv")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.markdown("## 🔍 Filter Data")
st.sidebar.markdown("---")

gender_filter = st.sidebar.selectbox("👤 Gender", ["All"] + list(df['gender'].unique()))
status_filter = st.sidebar.selectbox("🎯 Placement Status", ["All"] + list(df['status'].unique()))

min_marks = int(df['degree_p'].min())
max_marks = int(df['degree_p'].max())

marks_range = st.sidebar.slider("📊 Degree %", min_marks, max_marks, (min_marks, max_marks))

workex_filter = st.sidebar.selectbox("💼 Work Experience", ["All"] + list(df['workex'].unique()))

# -------------------------------
# FILTERING
# -------------------------------
filtered_df = df.copy()

if gender_filter != "All":
    filtered_df = filtered_df[filtered_df['gender'] == gender_filter]

if status_filter != "All":
    filtered_df = filtered_df[filtered_df['status'] == status_filter]

filtered_df = filtered_df[
    (filtered_df['degree_p'] >= marks_range[0]) &
    (filtered_df['degree_p'] <= marks_range[1])
]

if workex_filter != "All":
    filtered_df = filtered_df[filtered_df['workex'] == workex_filter]

# -------------------------------
# METRICS
# -------------------------------
st.subheader("📌 Key Metrics")

placed = filtered_df[filtered_df['status'] == 'Placed'].shape[0]
total = filtered_df.shape[0]

placement_rate = (placed / total) * 100 if total > 0 else 0
avg_salary = filtered_df['salary'].dropna().mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total", total)
col2.metric("Placed", placed)
col3.metric("Placement %", round(placement_rate, 2))
col4.metric("Avg Salary", round(avg_salary, 2) if not pd.isna(avg_salary) else 0)

# -------------------------------
# VISUALS
# -------------------------------
st.subheader("📊 Visual Analysis")
st.markdown("---")

FIG_SIZE = (3.2, 2.2)

def show_chart(fig):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.pyplot(fig, use_container_width=False)

# -------------------------------
# PIE
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🥧 Placement Ratio")

fig, ax = plt.subplots(figsize=FIG_SIZE)
ax.pie(
    filtered_df['status'].value_counts(),
    labels=filtered_df['status'].value_counts().index,
    autopct='%1.1f%%',
    colors=['#22c55e', '#ef4444']
)
plt.tight_layout()
show_chart(fig)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# BAR
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📊 Gender vs Placement")

fig, ax = plt.subplots(figsize=FIG_SIZE)
sns.countplot(x='gender', hue='status', data=filtered_df, palette='Set2', ax=ax)
plt.tight_layout()
show_chart(fig)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# HISTOGRAM
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📈 Degree % Distribution")

fig, ax = plt.subplots(figsize=FIG_SIZE)
sns.histplot(filtered_df['degree_p'], bins=20, kde=True, color='skyblue', ax=ax)
plt.tight_layout()
show_chart(fig)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# SALARY
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 💰 Salary Distribution")

fig, ax = plt.subplots(figsize=FIG_SIZE)
sns.histplot(filtered_df['salary'].dropna(), bins=20, color='orange', ax=ax)
plt.tight_layout()
show_chart(fig)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# BOXPLOT
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📦 Marks vs Placement")

fig, ax = plt.subplots(figsize=FIG_SIZE)
sns.boxplot(x='status', y='degree_p', data=filtered_df, palette='pastel', ax=ax)
plt.tight_layout()
show_chart(fig)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# HEATMAP
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🔥 Correlation Heatmap")

numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])

fig, ax = plt.subplots(figsize=(5, 3.5))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",                 # only 2 decimal points
    cmap="coolwarm",
    linewidths=0.5,            # spacing between boxes
    cbar_kws={"shrink": 0.7},  # smaller color bar
    annot_kws={"size": 7},     # smaller text
    ax=ax
)

# Rotate labels properly
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

plt.tight_layout()

# Center chart
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.pyplot(fig, use_container_width=False)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# DOWNLOAD
# -------------------------------
st.subheader("⬇ Download Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name='filtered_data.csv',
    mime='text/csv'
)