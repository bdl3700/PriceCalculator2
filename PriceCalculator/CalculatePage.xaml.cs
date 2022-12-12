namespace PriceCalculator;

public partial class CalculatePage : ContentPage
{
	public CalculatePage()
	{
		InitializeComponent();
	}

    private void CalculatePage_Loaded(object sender, EventArgs e)
    {
        double w = DeviceDisplay.Current.MainDisplayInfo.Width / 8;
        double h = DeviceDisplay.Current.MainDisplayInfo.Height / 2;

        Window.MinimumWidth = w;
        Window.MaximumWidth = w;
        Window.MinimumHeight = h;
        Window.MaximumHeight = h;

        Preferences.Set("height", h);
        Preferences.Set("width", w);
    }
}