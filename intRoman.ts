// Create a class to convert integers to roman numbers

class IntRoman {
    private romans = [['I', 'X', 'C', 'M'], ['V', 'L', 'D']];

    private oneToThree (integer: number, placeValue: number): string {
        /* 
            returns the roman equivalent for a number between one and three
        */
        return this.romans[0][placeValue - 1].repeat(integer);
    }

    private midSix(integer: number, placeValue: number): string {
        /* 
            returns the roman equivalent for a number between 4 and 8
        */
        let ans: string;
        const localPV  = placeValue - 1;
        ans = this.romans[1][localPV];
        
        if (integer === 4) {
            // add something to the front
            let prefix = this.romans[0][localPV];
            ans = `${prefix}${ans}`;
        } else if (integer > 5) {
            // add something to the back
            let suffix = this.romans[0][localPV];
            ans = `${ans}${suffix.repeat(integer - 5)}`;
        };

        return ans;
    }

    private nine (placeValue: number): string {
        /* 
            returns the roman equivalent of 9
        */
        const localPV = placeValue - 1;
        return `${this.romans[0][localPV]}${this.romans[0][localPV + 1]}`;
    }

    private resolute (integer: number): string {
        /* 
            map every single digit into it's eqivalent roman numeral
            then merge the results into one string
        */
        const integerAsArray = [...integer.toString()].map((int) => parseInt(int));
        integerAsArray.reverse();

        const resolution = integerAsArray.map((num, index) => {
            index++;

            if (num < 4) {
                // if num is in [1, 2, 3]
                return this.oneToThree(num, index);
            } else if (num > 3 && num < 9) {
                // if num is in [4, 5, 6, 7, 8]
                return this.midSix(num, index);
            } else if (num === 9) {
                // if num is 9
                return this.nine(index);
            };
        });

        resolution.reverse();

        return resolution.join('');   
    };

    toRoman (rawNumber: any): string {
        /* 
            Convert a single digit
        */
        const integer = parseInt(rawNumber);

        if (isNaN(integer))
            throw new Error('rawNumber is not a number');

        if (integer > 3999)
            throw new Error('does not support numbers over 3999');

        if (integer === 0)
            throw new Error('0 has no roman number equivalent');

        return this.resolute(integer);
    };

    toRomanArray (rawNumbersArray: any[]): string[] {
        /* 
            convert an array of digits
        */
        if (!Array.isArray(rawNumbersArray))
            throw new Error('Your input was not an array');
        
        return Array.from(rawNumbersArray, (item) => this.toRoman(item));
    };
};