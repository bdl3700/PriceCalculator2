using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PriceCalculator
{
    /// <summary>
    /// Represents an ItemType for use in calculating prices.
    /// Utilizes the sigmoid function to determine the appropriate margin for the input cost, then uses that to calculate a raw retail value.
    /// </summary>
    internal class ItemType
    {
        public string Name { get; set; }
        public char ShortcutKey { get; private set; }
        public double AValue { get; private set; }
        public double EValue { get; private set; }

        public double CalculateMargin(double cost)
        {
            if (cost > 0)
            {
                return this.AValue / (1 + Math.Pow(this.EValue, -cost));
            }
            return 0.0;
        }

        public double CalculateRetail(double cost)
        {
            if (cost > 0) { return cost/this.CalculateMargin(cost); }
            return 0.0;
        }

        /// <summary>
        /// Creates an ItemType to represent a class of retail item for calculating prices on.
        /// </summary>
        /// <param name="name">Type Name</param>
        /// <param name="shortcutKey">A char which the UI may map to a keystroke that can be used to quickly select this type in UI applications.</param>
        /// <param name="aValue">The value which will be utilized in the numerator of The Sigmoid Function in place of 1 (Represents the horizontal asymptote, in this context valid values will be in the range (0,1) exclusive.</param>
        /// <param name="eValue">The value which will be utilized in place of e in The Sigmoid Function (effects the rate at which the function approaches the asymptote, in this context valid values will be in the range (1, infinity) exclusive.</param>
        /// <exception cref="ArgumentException">Thrown when an AValue or EValue out of the appropriate range is input.</exception>
        public ItemType(string name, char shortcutKey, double aValue, double eValue)
        {
            if (aValue <= 0 || aValue >= 1 || eValue <= 1)
            {
                throw new ArgumentOutOfRangeException("Invalid ItemType Argument provided");
            }
            Name = name;
            ShortcutKey = shortcutKey;
            AValue = aValue;
            EValue = eValue;
        }
    }
}
