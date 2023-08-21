@app.route("/stats")
def stats():
    return render_template('stats.html')
def stats1():
    data = pd.read_csv('data.csv')
    
    # Select the column for the pie chart
    category_column = 'SEVERE_MENTAL_DISORDER_(SMD)'

    # Create a pie chart
    plt.pie(data[category_column], labels=data['DISTRICT '], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the chart to a BytesIO object
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close()

    return send_file(image_stream, mimetype='image/png')