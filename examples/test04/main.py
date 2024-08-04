import data_fetcher
import chart_creator
import chart_display

def main():
    # Fetch historical gold price data
    data = data_fetcher.fetch_gold_price_data()
    
    # Create the chart
    chart_path = chart_creator.create_chart(data)
    
    # Display the chart and save as PNG
    chart_display.show_and_save_chart(chart_path)

if __name__ == "__main__":
    main()