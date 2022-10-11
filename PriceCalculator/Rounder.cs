using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PriceCalculator
{
    internal class Rounder
    {
        /// <summary>
        /// A sorted array of tuples each containing two doubles, the first (and that upon which the list is sorted) a value to compare inputs against and the second a value to round items less than the first value to.
        /// </summary>
        public Tuple<double, double>[] RoundingThresholds { get; private set; }
        /// <summary>
        /// <para>The percentage of the value the input is rounded to which determines whether the input should be rounded up or down.</para>
        /// <para>Defaults to 0.3</para>
        /// </summary>
        public double RoundDownThreshold { get; private set; }
        public double Round(double input)
        {
            // Find the appropriate threshold
            Tuple<double, double> threshold = new Tuple<double,double>(0.0, 0.5);
            for (int i = 0; i < RoundingThresholds.Length; i++)
            {
                threshold = RoundingThresholds[i];
                if (threshold.Item1 > input) break;
            }

            // Round
            if ((input % threshold.Item2) / threshold.Item2 < RoundDownThreshold)
            {
                return input - (input % threshold.Item2);
            }
            return input + (threshold.Item2 - (input % threshold.Item2));
        }

        public Rounder(Tuple<double, double>[] roundingThresholds, double roundDownThreshold = .3)
        {
            if (roundingThresholds.Length < 1) throw new ArgumentException("At least one rounding threshold must be defined");
            if (roundDownThreshold <= 0 | roundDownThreshold >= 1) roundDownThreshold = .3;
            RoundingThresholds = roundingThresholds;
            RoundDownThreshold = roundDownThreshold;
        }
    }
}
