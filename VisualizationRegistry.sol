// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract VisualizationRegistry is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // This mapping will store hashes of registered visualizations
    mapping(bytes32 => bool) private _registeredHashes;

    constructor() ERC721("VisualizationRegistry", "VR") {}

    function registerVisualization(address owner, string memory tokenURI, bytes32 visualizationHash) 
        public 
        returns (uint256) 
    {
        // Ensure that this visualization has not been registered before
        require(!_registeredHashes[visualizationHash], "This visualization is already registered.");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        _mint(owner, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Mark this hash as registered
        _registeredHashes[visualizationHash] = true;

        return newTokenId;
    }
}
