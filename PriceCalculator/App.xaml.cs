using System.Diagnostics;

namespace PriceCalculator
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            MainPage = new AppShell();
        }

        protected override Window CreateWindow(IActivationState activationState)
        {
            var w = base.CreateWindow(activationState);

            // default values that will later be ovewritten by a fraction of the display's dimensions
            w.MinimumWidth = 300;
            w.MaximumWidth = 300;
            w.MinimumHeight =600;
            w.MaximumHeight = 600;
            return w;
        }
    }
}